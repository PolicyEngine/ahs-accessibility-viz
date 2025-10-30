"""
Download and process AHS microdata for accessibility visualization.

This script:
1. Downloads 2019 AHS national microdata (with accessibility module)
2. Creates summary tables by:
   - Building age (year built)
   - Structure type (units in structure)
   - Accessibility features
3. Exports lightweight JSON files for web visualization
"""

import os
import zipfile
import requests
import pandas as pd
import numpy as np
import json
from pathlib import Path

# URLs for AHS data
AHS_2019_URL = "https://www2.census.gov/programs-surveys/ahs/2019/AHS%202019%20National%20PUF%20v2.1%20Flat%20SAS.zip"
AHS_2023_URL = "https://www2.census.gov/programs-surveys/ahs/2023/AHS%202023%20National%20PUF%20v1.0%20Flat%20SAS.zip"

def download_ahs(url, year):
    """Download AHS microdata if not already downloaded."""
    filename = f"ahs_{year}_raw.zip"

    if os.path.exists(filename):
        print(f"✓ {filename} already exists")
        return filename

    print(f"Downloading AHS {year} data...")
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"✓ Downloaded {filename}")
    return filename

def load_ahs_2019():
    """Load and process 2019 AHS data with accessibility features."""
    print("\nProcessing 2019 AHS data...")

    # For now, we'll create placeholder data
    # TODO: Download and parse actual AHS microdata
    # zip_file = download_ahs(AHS_2019_URL, 2019)

    print("Note: Creating placeholder data structure")
    print("TODO: Implement actual AHS microdata processing")
    print("Variables needed from AHS:")
    print("  - BUILT: Year structure built")
    print("  - UNITSIZE: Units in structure")
    print("  - WEIGHT: Sampling weight")
    print("  - Accessibility variables from 2019 topical module")

    return create_example_summaries()

def create_example_summaries():
    """Create example summary data structure."""

    # Building age categories
    age_categories = [
        "Before 1960",
        "1960-1979",
        "1980-1999",
        "2000-2009",
        "2010 or later"
    ]

    # Structure types
    structure_types = [
        "Single-family detached",
        "2-4 units",
        "5-49 units",
        "50+ units"
    ]

    # Accessibility features (from AHS 2019 codebook)
    features = [
        "No-step entrance",
        "Single-floor living",
        "Wide doorways/hallways",
        "Accessible bathroom",
        "Accessible kitchen"
    ]

    # Create summary by building age
    age_summary = []
    for age in age_categories:
        for feature in features:
            age_summary.append({
                "age_category": age,
                "feature": feature,
                "percent_with_feature": np.random.uniform(20, 80),  # Placeholder
                "total_units": np.random.randint(5000000, 20000000)
            })

    # Create summary by structure type
    structure_summary = []
    for structure in structure_types:
        for feature in features:
            structure_summary.append({
                "structure_type": structure,
                "feature": feature,
                "percent_with_feature": np.random.uniform(20, 80),  # Placeholder
                "total_units": np.random.randint(5000000, 30000000)
            })

    return {
        "by_age": pd.DataFrame(age_summary),
        "by_structure": pd.DataFrame(structure_summary),
        "metadata": {
            "year": 2019,
            "source": "American Housing Survey",
            "note": "Placeholder data - requires actual AHS microdata processing"
        }
    }

def export_json(data, output_dir="processed"):
    """Export processed data as JSON files."""
    Path(output_dir).mkdir(exist_ok=True)

    # Export age summary
    age_file = f"{output_dir}/accessibility_by_age.json"
    data["by_age"].to_json(age_file, orient="records", indent=2)
    print(f"✓ Exported {age_file}")

    # Export structure summary
    structure_file = f"{output_dir}/accessibility_by_structure.json"
    data["by_structure"].to_json(structure_file, orient="records", indent=2)
    print(f"✓ Exported {structure_file}")

    # Export metadata
    metadata_file = f"{output_dir}/metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump(data["metadata"], f, indent=2)
    print(f"✓ Exported {metadata_file}")

if __name__ == "__main__":
    print("AHS Accessibility Data Processor")
    print("=" * 50)

    # Process 2019 data (with accessibility module)
    data = load_ahs_2019()

    # Export to JSON
    export_json(data)

    print("\n" + "=" * 50)
    print("✓ Processing complete!")
    print("\nNext steps:")
    print("1. Update process.py with actual AHS variable processing")
    print("2. Copy processed/*.json to ../src/data/")
    print("3. Run React app: npm run dev")
