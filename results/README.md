# Results Directory

This directory contains analysis outputs from DFS channel analysis. **Note**: Result files are not tracked in git as they are generated from reproducible code.

## Directory Structure

```
results/
├── README.md                          # This file
├── .gitkeep                          # Keeps empty folders in git
│
├── figures/                          # Publication-quality visualizations
│   ├── database-analysis/            # DFS selection validation plots
│   │   ├── climate_zone_distribution.svg
│   │   ├── tectonic_setting_analysis.svg
│   │   └── system_selection_validation.svg
│   │
│   ├── profile-analysis/             # Elevation profile plots
│   │   ├── rio_fragua_chorroso_profiles.svg
│   │   ├── canning_river_profiles.svg
│   │   ├── nabesna_river_profiles.svg
│   │   ├── brahmaputra_river_profiles.svg
│   │   ├── unnamed_iranian_dfs_profiles.svg
│   │   └── comparative_profile_analysis.svg
│   │
│   ├── cross-section-analysis/       # Width measurement plots
│   │   ├── rio_fragua_chorroso_widths.svg
│   │   ├── canning_river_widths.svg
│   │   ├── nabesna_river_widths.svg
│   │   ├── brahmaputra_river_widths.svg
│   │   ├── unnamed_iranian_dfs_widths.svg
│   │   └── comparative_width_trends.svg
│   │
│   ├── environmental-analysis/       # Environment distribution plots
│   │   ├── rio_fragua_chorroso_environments.svg
│   │   ├── canning_river_environments.svg
│   │   ├── nabesna_river_environments.svg
│   │   ├── brahmaputra_river_environments.svg
│   │   ├── unnamed_iranian_dfs_environments.svg
│   │   └── climate_environment_comparison.svg
│   │
│   └── statistical-summary/          # Multi-system comparisons
│       ├── ols_regression_results.svg
│       ├── lowess_smoothing_comparison.svg
│       ├── coefficient_variation_analysis.svg
│       └── multi_scale_summary.svg
│
├── tables/                           # Statistical summaries and data exports
│   ├── database-analysis/            # Site selection results
│   │   ├── modern_dfs_analysis_summary.xlsx
│   │   ├── selected_systems_validation.csv
│   │   └── climate_tectonic_distribution.xlsx
│   │
│   ├── profile-data/                 # Elevation measurements
│   │   ├── rio_fragua_chorroso_profile_data.xlsx
│   │   ├── canning_river_profile_data.xlsx
│   │   ├── nabesna_river_profile_data.xlsx
│   │   ├── brahmaputra_river_profile_data.xlsx
│   │   ├── unnamed_iranian_dfs_profile_data.xlsx
│   │   └── combined_profile_metrics.xlsx
│   │
│   ├── width-measurements/           # Cross-section data
│   │   ├── rio_fragua_chorroso_widths.xlsx
│   │   ├── canning_river_widths.xlsx
│   │   ├── nabesna_river_widths.xlsx
│   │   ├── brahmaputra_river_widths.xlsx
│   │   ├── unnamed_iranian_dfs_widths.xlsx
│   │   └── width_trend_statistics.xlsx
│   │
│   ├── environmental-data/           # Environment quantification
│   │   ├── rio_fragua_chorroso_environment_areas.xlsx
│   │   ├── canning_river_environment_areas.xlsx
│   │   ├── nabesna_river_environment_areas.xlsx
│   │   ├── brahmaputra_river_environment_areas.xlsx
│   │   ├── unnamed_iranian_dfs_environment_areas.xlsx
│   │   └── environmental_proportions_summary.xlsx
│   │
│   └── statistical-analysis/         # Regression and trend results
│       ├── ols_regression_coefficients.xlsx
│       ├── lowess_smoothing_parameters.xlsx
│       ├── significance_test_results.xlsx
│       ├── coefficient_variation_summary.xlsx
│       └── multi_scale_statistics.xlsx
│
└── system-outputs/                   # Individual system complete results
    ├── rio_fragua_chorroso/          # Tropical system (Colombia)
    │   ├── profile_analysis/
    │   ├── width_measurements/
    │   ├── environmental_analysis/
    │   ├── statistical_summary/
    │   └── final_report.pdf
    │
    ├── canning_river/                # Polar system (Alaska)
    │   ├── profile_analysis/
    │   ├── width_measurements/
    │   ├── environmental_analysis/
    │   ├── statistical_summary/
    │   └── final_report.pdf
    │
    ├── nabesna_river/                # Continental system (Alaska)
    │   ├── profile_analysis/
    │   ├── width_measurements/
    │   ├── environmental_analysis/
    │   ├── statistical_summary/
    │   └── final_report.pdf
    │
    ├── brahmaputra_river/            # Subtropical system (India)
    │   ├── profile_analysis/
    │   ├── width_measurements/
    │   ├── environmental_analysis/
    │   ├── statistical_summary/
    │   └── final_report.pdf
    │
    └── unnamed_iranian_dfs/          # Drylands system (Iran)
        ├── profile_analysis/
        ├── width_measurements/
        ├── environmental_analysis/
        ├── statistical_summary/
        └── final_report.pdf
```

## Output Categories

### Publication Figures
- **Format**: SVG (vector graphics) for publication quality
- **Style**: SciencePlots with Paul Tol colorblind-friendly palette
- **Resolution**: 300 DPI when exported to raster formats
- **Naming**: Descriptive with system names and analysis type

### Data Tables
- **Primary Format**: Excel (.xlsx) with multiple sheets
- **Secondary Format**: CSV for interoperability
- **Content**: Raw measurements, statistics, metadata
- **Structure**: Consistent column naming across systems

### Individual Reports
- **Format**: PDF summaries for each system
- **Content**: Complete analysis workflow results
- **Audience**: System-specific detailed examination
- **Generation**: Automated from analysis notebooks

## File Naming Convention

### System Names
- `rio_fragua_chorroso` - Río Fragua Chorroso (Tropical, Colombia)
- `canning_river` - Canning River (Polar, Alaska)
- `nabesna_river` - Nabesna River (Continental, Alaska)
- `brahmaputra_river` - Brahmaputra River (Subtropical, India)
- `unnamed_iranian_dfs` - Unnamed Iranian DFS (Drylands, Iran)

### Analysis Types
- `profiles` - Elevation profile analysis
- `widths` - Cross-section width measurements  
- `environments` - Environmental area quantification
- `statistics` - Statistical trend analysis
- `comparison` - Multi-system comparative analysis

### Example Files
```
rio_fragua_chorroso_profile_analysis.svg
canning_river_width_trends.xlsx
multi_system_ols_regression_summary.xlsx
climate_zone_environmental_comparison.svg
```

## Analysis Workflow Outputs

### 1. Database Selection Analysis
- Validation of system selection methodology
- Climate zone and tectonic setting representation
- Statistical justification for chosen systems

### 2. Profile Analysis
- LOWESS-smoothed elevation profiles
- Gradient calculations and concavity metrics
- Longitudinal trend identification

### 3. Cross-Section Analysis
- Channel belt and active channel width measurements
- OLS regression trend analysis
- Statistical significance testing (p < 0.05)

### 4. Environmental Analysis
- Area quantification of environment types:
  - Wetted channels (dry riverbeds for Iran system)
  - Vegetated bars and islands
  - Unvegetated sediment bars
  - Total bar complexes

### 5. Multi-Scale Statistics
- System-scale: Complete DFS analysis
- Domain-scale: Proximal/medial/distal comparisons
- Cross-section-scale: Transverse measurement trends
- Reach-scale: Local segment analysis

## Quality Control

### Data Validation
- Automated checks for missing values
- Statistical outlier detection
- Cross-system consistency verification

### Figure Standards
- Consistent axis labels and units
- Legend placement and readability
- Color accessibility (Paul Tol palette)
- Grid lines and professional styling

### Table Standards
- Standardized column headers
- Consistent decimal precision
- Metadata and units documentation
- Cross-referencing capabilities

## Usage Notes

### Regeneration
All results can be regenerated by running the complete analysis pipeline:
```bash
# Run complete workflow
jupyter notebook code/statistical-analysis/main_dfs_analysis.ipynb
```

### Dependencies
Results depend on processed data in `data/` directory and proper execution of:
1. Database selection analysis
2. ArcGIS profile extraction
3. Statistical analysis pipeline
4. Visualization generation

### Version Control
- Results are excluded from git tracking (see .gitignore)
- Reproducible through code execution
- Timestamped outputs for version tracking

## Applications

These results support:
- **Academic Publication**: Complete figure and table sets
- **Comparative Analysis**: Cross-climate system evaluation  
- **Methodology Validation**: Statistical rigor demonstration
- **Future Research**: Baseline data for extended studies

## Support

For questions about result interpretation or regeneration:
- Consult analysis notebook documentation
- Review statistical methodology in code comments
- Check result validation against expected ranges
- Open repository issues for technical problems
