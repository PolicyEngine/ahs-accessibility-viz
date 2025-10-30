# AHS Accessibility Visualization

Interactive visualization of housing accessibility features from the American Housing Survey, analyzing trends by building age and structure type.

## Background

This tool replicates and updates HUD's 2011 analysis ["Accessibility of America's Housing Stock"](https://www.huduser.gov/portal/sites/default/files/pdf/accessibility-america-housingStock.pdf) using more recent AHS data.

**Key finding from original study**: Units in newer and large multifamily buildings are more likely to have accessibility features than units in smaller apartment buildings, single-family homes, or older construction.

## Data Sources

- **2019 AHS National Public Use File**: Accessibility Topical Module
- **Sample**: 63,000+ housing units
- **Coverage**: Weighted estimates representing 127 million occupied housing units nationwide
- **Variables analyzed**: No-step entrance, wheelchair ramp, wide doorways/hallways, accessible bathroom

## Features

- **Building age analysis**: Accessibility features by year built (pre-1960 through 2010+)
- **Structure type comparison**: Single-family, 2-4 units, 5-49 units, 50+ units, mobile homes
- **Real microdata**: Processed from AHS 2019 Public Use File with sampling weights
- **Interactive visualizations**: Filter by accessibility feature to explore trends

## Project Structure

```
ahs-accessibility-viz/
├── data/
│   ├── process_real.py      # Process AHS 2019 microdata (real data)
│   ├── process.py          # Original placeholder script
│   ├── requirements.txt     # Python dependencies
│   ├── ahs2019n.csv        # Downloaded microdata (936MB, not in git)
│   └── processed/          # Generated summary tables (JSON)
├── src/
│   ├── components/         # React components for visualizations
│   ├── data/              # Processed data (JSON, copied from data/processed)
│   └── App.jsx            # Main app
└── .github/workflows/      # GitHub Actions for deployment
```

## Development

### Process data from scratch

```bash
cd data
pip install -r requirements.txt

# Download and process real AHS 2019 data
python process_real.py

# Copy processed data to React app
cp processed/*.json ../src/data/
```

Note: The AHS microdata file (ahs2019n.csv) is 936MB and will be downloaded automatically by the script.

### Run app

```bash
npm install
npm run dev
```

### Deploy

```bash
npm run build
npm run deploy
```

## License

MIT
