# Data Directory

This directory contains input datasets for DFS channel analysis. **Note**: Data files are not tracked in git due to size and licensing restrictions.

## Directory Structure

```
data/
├── README.md                             # This file
├── .gitkeep                              # Keeps empty folders in git
│
├── hartley_et_al_modern_dfs.xlsx         # Modern DFS database
│   └── Global_DFS_database.kmz           # Spatial visualisation file
│
├── rio_fragua_chorroso_dfs_analysis_data.xlsx    # System-specific analysis data
│   ├── channel_profile                      # For channel gradient analysis
│   ├── cross_section_scale                  # Channel belt, active channel widths and their ratios
│   ├── system_scale                         # Whole DFS environment areas
│   ├── domain_scale                         # Proximal/medial/distal environment areas
│   └── reach_scale                          # Reach-scale environment areas
│
├── canning_dfs_analysis_data.xlsx         # System-specific analysis data
│   ├── channel_profile
│   ├── cross_section_scale
│   ├── system_scale
│   ├── domain_scale
│   └── reach_scale
│
├── nabesna_dfs_analysis_data.xlsx         # System-specific analysis data
│   ├── channel_profile
│   ├── cross_section_scale
│   ├── system_scale
│   ├── domain_scale
│   └── reach_scale
│
├── brahmaputra_dfs_analysis_data.xlsx     # System-specific analysis data
│   ├── channel_profile
│   ├── cross_section_scale
│   ├── system_scale
│   ├── domain_scale
│   └── reach_scale
│
└── unnamed_iranian_dfs_analysis_data.xlsx   # System-specific analysis data
    ├── channel_profile
    ├── cross_section_scale
    ├── system_scale
    ├── domain_scale
    └── reach_scale
```

## Data Sources

**`hartley_et_al_modern_dfs.xlsx`**  
- Global compilation of 415 modern distributive fluvial systems
- Statistical and morphometric data for site selection analysis
- Associated with: Hartley, A.J., Weissmann, G.S., Nichols, G.J. and Warwick, G.L. (2010) 'Large distributive fluvial systems: characteristics, distribution, and controls on development', *Journal of Sedimentary Research*, 80(2), pp.167-183.

**`Global_DFS_database.kmz`**  
- Google Earth KMZ file for spatial visualisation of distributive fluvial systems
- Geographic locations (apex and toe coordinates) of documented DFS
- Compatible with Google Earth Pro and GIS software
- Associated with: Hartley, A.J., Weissmann, G.S., Nichols, G.J. and Warwick, G.L. (2010) 'Large distributive fluvial systems: characteristics, distribution, and controls on development', *Journal of Sedimentary Research*, 80(2), pp.167-183.

### Statistical Analysis Datasets

Each system's analysis data is organised in standardised Excel files with multiple sheets for multi-scale analysis:

#### Sheet Structure (5 sheets per system)
- **`channel_profile`**: Elevation data for LOWESS profile analysis and gradient calculation
- **`cross_section_scale`**: Channel belt width and active channel width measurements for OLS trend analysis
- **`system_scale`**: Whole DFS environment areas (wetted channel, vegetated bars, unvegetated bars, bar complex)
- **`domain_scale`**: Environment areas by domain - Proximal (0-33.3%), Medial (33.3-66.7%), Distal (66.7-100%)
- **`reach_scale`**: Reach-scale environment areas for downstream trend analysis (OLS → R², p-value, CV)

#### Analysis Data Usage
- **Profile Analysis**: `channel_profile` sheet → LOWESS smoothing → gradient plots
- **Width Trend Analysis**: `cross_section_scale` sheet → OLS regression → R², p-value, CV statistics  
- **Environmental Analysis**: `system_scale`, `domain_scale`, `reach_scale` sheets → Multi-scale spatial variability analysis
- **Comparative Analysis**: Combined `cross_section_scale` data from all systems → channel belt to active channel width ratios

## Data Acquisition Workflow

### For Researchers Using This Methodology

**Step 1: Identify Study Systems**
- Use `Global_DFS_database.kmz` to locate potential DFS
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
- **Example**: `rio_fragua_chorroso_analysis_data.xlsx`
- **System Names (Climate Order)**: 
  - `rio_fragua_chorroso_dfs` (Tropical, Colombia)
  - `canning_dfs` (Polar, Alaska)
  - `nabesna_dfs` (Continental, Alaska)
  - `brahmaputra_dfs` (Subtropical, India)
  - `unnamed_iranian_dfs` (Drylands, Iran)

### Excel Sheet Organisation
- **Standardised structure**: All systems follow identical 5-sheet format
- **Multi-scale framework**: System/domain/reach scale data organization
- **Analysis-ready**: Direct input for statistical analysis workflows
- **Consistent formatting**: Uniform column headers and data types

### Quality Control
- **Geodatabase validation**: Quality-controlled through ArcGIS Pro digitisation protocols
- **Measurement consistency**: Standardised methods across all systems
- **Data completeness**: Verified coverage for all required analysis scales

## Access and Licensing

### Publicly Available Data
- **Sentinel-2**: Open access via USGS
- **SRTM**: Public domain via NASA/USGS
- **ArcticDEM**: Open access via Polar Geospatial Center

### Generated Data
- **Analysis datasets**: Created as part of this research
- **Processed measurements**: Derived from public sources with added analytical value

## Getting Started

### For New Researchers
1. **Review methodology**: Examine `code/` documentation for complete workflow
2. **Identify study systems**: Use KMZ file to locate potential DFS
3. **Acquire source data**: Follow data acquisition workflow
4. **Apply digitisation protocol**: Use ArcGIS Pro workflow
5. **Generate analysis data**: Export to standardised Excel format
6. **Run statistical analysis**: Use provided analysis pipeline

### For This Study Analysis
1. **Load analysis datasets**: Excel files ready for statistical processing
2. **Configure system parameters**: Use `code/config/` templates
3. **Run analysis workflow**: Execute statistical analysis pipeline
4. **Generate results**: Produce publication-quality outputs

## Support

For questions about data structure or acquisition workflow:
- Review analysis pipeline documentation in `code/statistical-analysis/`
- Consult individual tool documentation in respective code folders
- Open repository issues for technical problems or clarifications
