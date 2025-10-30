# AHS Accessibility Visualization

Interactive visualization of housing accessibility features from the American Housing Survey, analyzing trends by building age and structure type.

## Background

This tool replicates and updates HUD's 2011 analysis ["Accessibility of America's Housing Stock"](https://www.huduser.gov/portal/sites/default/files/pdf/accessibility-america-housingStock.pdf) using more recent AHS data.

**Key finding from original study**: Units in newer and large multifamily buildings are more likely to have accessibility features than units in smaller apartment buildings, single-family homes, or older construction.

## Data Sources

- **2019 AHS**: Latest year with Accessibility Topical Module
- **2023 AHS**: Latest available data (accessibility module not included)
- **Coverage**: ~75,000 housing units nationally

## Features

- Building age analysis (year built)
- Structure type comparison (single-family, 2-4 units, 5-49 units, 50+ units)
- Accessibility feature trends (2011 → 2019)
- Interactive charts and filters

## Project Structure

```
ahs-accessibility-viz/
├── data/
│   ├── process.py          # Download and process AHS microdata
│   ├── requirements.txt     # Python dependencies
│   └── processed/          # Generated summary tables (JSON)
├── src/
│   ├── components/         # React components
│   ├── data/              # Processed data (copied from data/processed)
│   └── App.jsx            # Main app
└── public/                # Static assets
```

## Development

### Process data

```bash
cd data
pip install -r requirements.txt
python process.py
```

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
