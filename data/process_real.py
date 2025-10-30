"""
Process real AHS 2019 microdata for accessibility visualization.

This script:
1. Loads 2019 AHS national microdata
2. Identifies accessibility features from the topical module
3. Creates weighted summary tables by building age and structure type
4. Exports JSON files for web visualization
"""

import pandas as pd
import numpy as np
import json
from pathlib import Path

# Mapping for UNITSIZE (units in structure)
UNITSIZE_MAP = {
    '1': '1 unit (single-family detached)',
    '2': '1 unit (single-family attached)',
    '3': '2 units',
    '4': '3-4 units',
    '5': '5-9 units',
    '6': '10-19 units',
    '7': '20-49 units',
    '8': '50+ units',
    '9': 'Mobile home/trailer/other',
}

# Recode into broader categories for visualization
UNITSIZE_BROAD = {
    '1': 'Single-family detached',
    '2': 'Single-family attached',
    '3': '2-4 units',
    '4': '2-4 units',
    '5': '5-49 units',
    '6': '5-49 units',
    '7': '5-49 units',
    '8': '50+ units',
    '9': 'Mobile home/other',
}

# Building age categories
def categorize_age(year_built):
    """Categorize year built into age groups."""
    if pd.isna(year_built) or year_built < 0:
        return None
    if year_built < 1960:
        return 'Before 1960'
    elif year_built < 1980:
        return '1960-1979'
    elif year_built < 2000:
        return '1980-1999'
    elif year_built < 2010:
        return '2000-2009'
    else:
        return '2010 or later'

# Accessibility features mapping
# Values: 1 = Yes, 2 = No, -6 = Not applicable, -9 = Not reported
ACCESSIBILITY_VARS = {
    'NOSTEP': 'No-step entrance',
    'HARAMP': 'Wheelchair ramp',
    'MHWIDE': 'Wide doorways/hallways',
    'HMRACCESS': 'Accessible bathroom',
}

# Additional difficulty accessing features (reverse-coded)
DIFFICULTY_VARS = {
    'HAGETHOME': 'Difficulty entering home',
    'HAGETKIT': 'Difficulty using kitchen',
    'HAGETBATH': 'Difficulty using bathroom',
    'HAGETBED': 'Difficulty using bedroom',
}

def load_and_process_data():
    """Load AHS data and process accessibility features."""
    print("Loading AHS 2019 microdata...")

    # Load only needed columns
    columns_needed = ['WEIGHT', 'YRBUILT', 'UNITSIZE'] + \
                     list(ACCESSIBILITY_VARS.keys()) + \
                     list(DIFFICULTY_VARS.keys())

    df = pd.read_csv('ahs2019n.csv', usecols=columns_needed, dtype=str)

    # Convert weight and year built to numeric
    df['WEIGHT'] = pd.to_numeric(df['WEIGHT'], errors='coerce')
    df['YRBUILT'] = pd.to_numeric(df['YRBUILT'], errors='coerce')

    print(f"Loaded {len(df):,} housing units")

    # Clean string quotes from coded values
    for col in df.columns:
        if col not in ['WEIGHT', 'YRBUILT']:
            df[col] = df[col].str.strip("'")

    # Create age and structure categories
    df['age_category'] = df['YRBUILT'].apply(categorize_age)
    df['structure_type'] = df['UNITSIZE'].map(UNITSIZE_BROAD)

    # Filter to valid cases
    df = df[df['WEIGHT'] > 0].copy()
    df = df[df['age_category'].notna()].copy()
    df = df[df['structure_type'].notna()].copy()

    print(f"After filtering: {len(df):,} housing units")
    print(f"Total weighted units: {df['WEIGHT'].sum()/1e6:.1f}M")

    return df

def calculate_feature_prevalence(df, group_var, feature_var, feature_name):
    """Calculate weighted prevalence of a feature by group."""

    # Consider feature present if value is '1' (Yes)
    # Missing values (-6, -9, NaN) are treated as unknown/NA
    df_valid = df[df[feature_var].isin(['1', '2'])].copy()
    df_valid['has_feature'] = (df_valid[feature_var] == '1').astype(int)

    # Calculate weighted percentages
    grouped = df_valid.groupby(group_var).apply(
        lambda x: pd.Series({
            'percent_with_feature': 100 * (x['has_feature'] * x['WEIGHT']).sum() / x['WEIGHT'].sum(),
            'total_units': x['WEIGHT'].sum()
        })
    ).reset_index()

    grouped['feature'] = feature_name

    return grouped

def generate_summaries(df):
    """Generate summary tables by age and structure type."""

    summaries_by_age = []
    summaries_by_structure = []

    print("\nCalculating accessibility feature prevalence...")

    for var_name, feature_name in ACCESSIBILITY_VARS.items():
        if var_name in df.columns:
            print(f"  - {feature_name}")

            # By age
            age_summary = calculate_feature_prevalence(df, 'age_category', var_name, feature_name)
            summaries_by_age.append(age_summary)

            # By structure
            structure_summary = calculate_feature_prevalence(df, 'structure_type', var_name, feature_name)
            summaries_by_structure.append(structure_summary)

    # Combine all summaries
    by_age_df = pd.concat(summaries_by_age, ignore_index=True)
    by_structure_df = pd.concat(summaries_by_structure, ignore_index=True)

    return {
        'by_age': by_age_df,
        'by_structure': by_structure_df,
        'metadata': {
            'year': 2019,
            'source': 'American Housing Survey 2019 (Accessibility Topical Module)',
            'total_units': int(df['WEIGHT'].sum()),
            'sample_size': len(df),
            'features_analyzed': list(ACCESSIBILITY_VARS.values()),
            'note': 'Percentages based on weighted estimates. Missing/not applicable responses excluded.'
        }
    }

def export_json(data, output_dir="processed"):
    """Export processed data as JSON files."""
    Path(output_dir).mkdir(exist_ok=True)

    # Export age summary
    age_file = f"{output_dir}/accessibility_by_age.json"
    data["by_age"].to_json(age_file, orient="records", indent=2)
    print(f"\n✓ Exported {age_file}")

    # Export structure summary
    structure_file = f"{output_dir}/accessibility_by_structure.json"
    data["by_structure"].to_json(structure_file, orient="records", indent=2)
    print(f"✓ Exported {structure_file}")

    # Export metadata
    metadata_file = f"{output_dir}/metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump(data["metadata"], f, indent=2)
    print(f"✓ Exported {metadata_file}")

    # Print sample statistics
    print("\n" + "="*60)
    print("Sample statistics by building age:")
    print("="*60)
    for age in data["by_age"]['age_category'].unique():
        age_data = data["by_age"][data["by_age"]['age_category'] == age]
        if len(age_data) > 0:
            units = age_data['total_units'].iloc[0]
            print(f"{age:20s}: {units/1e6:6.1f}M units")

    print("\n" + "="*60)
    print("Sample statistics by structure type:")
    print("="*60)
    for structure in data["by_structure"]['structure_type'].unique():
        structure_data = data["by_structure"][data["by_structure"]['structure_type'] == structure]
        if len(structure_data) > 0:
            units = structure_data['total_units'].iloc[0]
            print(f"{structure:25s}: {units/1e6:6.1f}M units")

if __name__ == "__main__":
    print("AHS 2019 Accessibility Data Processor")
    print("=" * 60)

    # Load and process data
    df = load_and_process_data()

    # Generate summaries
    data = generate_summaries(df)

    # Export to JSON
    export_json(data)

    print("\n" + "=" * 60)
    print("✓ Processing complete!")
    print("\nNext steps:")
    print("1. Copy processed/*.json to ../src/data/")
    print("2. Run React app: npm run dev")
    print("3. Verify visualizations show real data")
