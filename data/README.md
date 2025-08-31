# Data Directory

This directory contains input datasets for DFS channel analysis. **Note**: Data files are not tracked in git due to size and licensing restrictions.

## Directory Structure

```
data/
├── README.md                           # This file
├── .gitkeep                           # Keeps empty folders in git
│
├── reference-data/                    # External datasets
│   ├── hartley_et_al_modern_dfs.xlsx # Modern DFS database
│   └── Global_DFS_database.kmz        # Spatial visualisation file
│
├── analysis-data/                     # Statistical analysis datasets
│   ├── rio_fragua_chorroso_analysis_data.xlsx
│   │   ├── channel_profile            # For channel gradient analysis
│   │   ├── cross_section_scale        # Channel belt, active channel widths and their ratios
│   │   ├── system_scale               # Whole DFS environment areas
│   │   ├── domain_scale               # Proximal/medial/distal environment areas
│   │   └── reach_scale                # Reach-scale environment areas
│   ├── canning_river_analysis_data.xlsx
│   │   ├── channel_profile            # For channel gradient analysis
│   │   ├── cross_section_scale        # Channel belt, active channel widths and their ratios
│   │   ├── system_scale               # Whole DFS environment areas
│   │   ├── domain_scale               # Proximal/medial/distal environment areas
│   │   └── reach_scale                # Reach-scale environment areas
│   ├── nabesna_river_analysis_data.xlsx
│   │   ├── channel_profile            # For channel gradient analysis
│   │   ├── cross_section_scale        # Channel belt, active channel widths and their ratios
│   │   ├── system_scale               # Whole DFS environment areas
│   │   ├── domain_scale               # Proximal/medial/distal environment areas
│   │   └── reach_scale                # Reach-scale environment areas
│   ├── brahmaputra_river_analysis_data.xlsx
│   │   ├── channel_profile            # For channel gradient analysis
│   │   ├── cross_section_scale        # Channel belt, active channel widths and their ratios
│   │   ├── system_scale               # Whole DFS environment areas
│   │   ├── domain_scale               # Proximal/medial/distal environment areas
│   │   └── reach_scale                # Reach-scale environment areas
│   └── unnamed_iranian_dfs_analysis_data.xlsx
│       ├── channel_profile            # For channel gradient analysis
│       ├── cross_section_scale        # Channel belt, active channel widths and their ratios
│       ├── system_scale               # Whole DFS environment areas
│       ├── domain_scale               # Proximal/medial/distal environment areas
│       └── reach_scale                # Reach-scale environment areas
│
└── processed/                         # Intermediate processing files
    └── temporary-outputs/             # Temporary analysis files
```
```

## Data Acquisition Workflow

### For Researchers Using This Methodology

**Step 1: Identify Study Systems**
- Use `reference-data/Global_DFS_database.kmz` to locate potential DFS
- Select systems based on research objectives and data availability

**Step 2: Acquire Source Data**
- **Satellite Imagery**: Download Sentinel-2 from USGS EarthExplorer
- **Elevation Data**: Use provided Google Earth Engine scripts
  - `code/google-earth-engine/gee_elevation_download.js` (SRTM/ArcticDEM)
  - `code/google-earth-engine/gee_sentinel2_complete_coverage.js` (if needed)

**Step 3: Manual Digitisation (ArcGIS Pro)**
- Create geodatabase for each system
- Digitise channel centerlines, channel belts, environmental features
- Extract measurements using `code/arcgis-tools/channel_profile_extraction.py`
- Export to analysis-ready Excel format following standardised sheet structure

**Step 4: Statistical Analysis**
- Place Excel files in `analysis-data/` folder
- Run analysis using `code/statistical-analysis/` workflow

### For This Study (Completed Analysis)
- Source imagery and elevation data were acquired and processed
- Manual digitisation completed in ArcGIS Pro geodatabases
- Final analysis-ready datasets provided in `analysis-data/` folder
- Raw imagery and elevation files not included due to size constraints

## Usage Notes

### File Naming Convention
- **Format**: `{system_name}_{data_type}.{extension}`
- **Example**: `rio_fragua_chorroso_sentinel2.tif`
- **System Names (Climate Order)**: 
  - `rio_fragua_chorroso` (Tropical, Colombia)
  - `canning_river` (Polar, Alaska)
  - `nabesna_river` (Continental, Alaska)
  - `brahmaputra_river` (Subtropical, India)
  - `unnamed_iranian_dfs` (Drylands, Iran)

### Coordinate Systems
- **Satellite/Elevation**: WGS84 (EPSG:4326)
- **Vector Data**: Appropriate UTM zone for each system
- **Processing**: Reprojected as needed for analysis

### Data Quality
- **Imagery**: Visually inspected for cloud cover and completeness
- **Elevation**: Validated against known elevation points
- **Vector**: Quality-controlled through systematic digitisation protocols

## Access and Licensing

### Publicly Available Data
- **Sentinel-2**: Open access via USGS
- **SRTM**: Public domain via NASA/USGS
- **ArcticDEM**: Open access via Polar Geospatial Center

### Generated Data
- **Vector datasets**: Created as part of this research
- **Processed data**: Derived from public sources with added value

## Getting Started

1. **Create data directories**: Run the provided setup script
2. **Download imagery**: Use Google Earth Engine scripts
3. **Acquire elevation data**: Run elevation download utilities  
4. **Perform digitisation**: Follow ArcGIS workflow documentation
5. **Validate data**: Check completeness and quality before analysis

## Support

For questions about data acquisition or processing, please refer to:
- Individual folder README files
- Code documentation in respective analysis scripts
- Repository issues for technical problems
