# Statistical Analysis

Multi-scale statistical analysis of distributive fluvial systems (DFSs) using manual digitisation data. This module processes channel geometry, environmental distributions, and downstream trends across five climate zones using standardised methodology.

## Directory Structure

```
statistical-analysis/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
│
├── system-notebooks/                  # Interactive analysis (Jupyter)
│   ├── rio_fragua_chorroso_analysis.ipynb      # Tropical system (Colombia)
│   ├── canning_river_analysis.ipynb            # Polar system (Alaska)
│   ├── nabesna_river_analysis.ipynb            # Continental system (Alaska)
│   ├── brahmaputra_river_analysis.ipynb        # Subtropical system (India)
│   └── unnamed_iranian_dfs_analysis.ipynb      # Drylands system (Iran)
│
├── system-scripts/                    # Python script equivalents
│   ├── rio_fragua_chorroso_analysis.py         # Batch processing version
│   ├── canning_river_analysis.py               # Batch processing version
│   ├── nabesna_river_analysis.py               # Batch processing version
│   ├── brahmaputra_river_analysis.py           # Batch processing version
│   └── unnamed_iranian_dfs_analysis.py         # Batch processing version
│
├── comparative-analysis/              # Cross-system comparisons
│   ├── channel_belt_active_ratio_analysis.ipynb  # Combined 5-system analysis
│   └── channel_belt_active_ratio_analysis.py     # Script version
│
├── src/                              # Reusable Python modules
│   ├── __init__.py                   # Package initialization
│   ├── data_loader.py                # Load system spreadsheets from ../data/
│   ├── profile_analysis.py           # LOWESS smoothing for channel gradients
│   ├── trend_analysis.py             # OLS regression (R², p-value, CV)
│   ├── multi_scale_analysis.py       # System/Domain/Reach scale processing
│   └── visualisation.py             # Publication-quality plotting functions
│
└── configs/                          # System-specific configuration files
    ├── rio_fragua_chorroso_config.py # Tropical system parameters
    ├── canning_river_config.py       # Polar system parameters
    ├── nabesna_river_config.py       # Continental system parameters
    ├── brahmaputra_river_config.py   # Subtropical system parameters
    └── unnamed_iranian_dfs_config.py # Drylands system parameters
```

## Data Structure

All analysis datasets are stored in the centralized `../data/` directory with standardized Excel file structure:

```
../data/
├── rio_fragua_chorroso_analysis_data.xlsx
│   ├── channel_profile             # For LOWESS profile analysis
│   ├── cross_section_scale         # Channel belt & active channel widths
│   ├── system_scale                # Whole DFS environment areas
│   ├── domain_scale                # Proximal/medial/distal environment areas
│   └── reach_scale                 # Reach-scale environment areas
├── canning_river_analysis_data.xlsx
│   ├── channel_profile             # For LOWESS profile analysis
│   ├── cross_section_scale         # Channel belt & active channel widths
│   ├── system_scale                # Whole DFS environment areas
│   ├── domain_scale                # Proximal/medial/distal environment areas
│   └── reach_scale                 # Reach-scale environment areas
├── nabesna_river_analysis_data.xlsx
│   ├── channel_profile             # For LOWESS profile analysis
│   ├── cross_section_scale         # Channel belt & active channel widths
│   ├── system_scale                # Whole DFS environment areas
│   ├── domain_scale                # Proximal/medial/distal environment areas
│   └── reach_scale                 # Reach-scale environment areas
├── brahmaputra_river_analysis_data.xlsx
│   ├── channel_profile             # For LOWESS profile analysis
│   ├── cross_section_scale         # Channel belt & active channel widths
│   ├── system_scale                # Whole DFS environment areas
│   ├── domain_scale                # Proximal/medial/distal environment areas
│   └── reach_scale                 # Reach-scale environment areas
└── unnamed_iranian_dfs_analysis_data.xlsx
    ├── channel_profile             # For LOWESS profile analysis
    ├── cross_section_scale         # Channel belt & active channel widths
    ├── system_scale                # Whole DFS environment areas
    ├── domain_scale                # Proximal/medial/distal environment areas
    └── reach_scale                 # Reach-scale environment areas
```

## Analysis Framework

### Individual System Analysis

Each system follows the same standardised analytical workflow:

#### 1. Profile Analysis
- **Input**: `channel_profile` sheet from system Excel file
- **Method**: LOWESS smoothing for channel gradient calculation
- **Output**: Smoothed elevation profiles and gradient plots

#### 2. Downstream Trend Analysis
- **Channel belt width trends**
  - Input: `cross_section_scale` sheet
  - Method: OLS regression
  - Statistics: R², p-value, CV (Coefficient of Variation)
  
- **Active channel width trends** (wetted channel or dry riverbed)
  - Input: `cross_section_scale` sheet  
  - Method: OLS regression
  - Statistics: R², p-value, CV
  
- **Cross-section scale analysis**
  - Transverse measurements at 5% intervals
  - Statistical trend identification
  
- **Reach scale analysis**
  - Input: `reach_scale` sheet
  - Method: OLS regression
  - Statistics: R², p-value, CV

#### 3. Multi-Scale Spatial Variability

**System-Scale Analysis**
- Input: `system_scale` sheet
- Analysis: Whole DFS environment quantification
- Output: Complete system environmental statistics

**Domain-Scale Analysis** 
- Input: `domain_scale` sheet
- Analysis: Proximal (0-33.3%), Medial (33.3-66.7%), Distal (66.7-100%) breakdown
- Output: Domain-specific environmental analysis

**Reach-Scale Analysis**
- Input: `reach_scale` sheet
- Method: OLS regression for downstream trends
- Statistics: R², p-value, CV for each environment type
- Output: Reach-scale environmental trend analysis

### Example Output Format

**Environment Analysis Results:**

| Environment | Area (km²) | R² | P | CV (%) | Min | Max |
|-------------|------------|----|----|--------|-----|-----|
| **A. Río Fragua Chorroso** ||||||| 
| Wetted channel | 0.8 | 2.5 | 0.457 | 0.001 | 30 | - |
| Bar complex | 0.4 | 10.5 | 0.404 | 0.003 | 107 | - |
| Vegetated bar | 0.0 | 8.8 | 0.397 | 0.004 | 134 | - |
| Unvegetated bar | 0.2 | 2.6 | 0.289 | 0.018 | 65 | - |

## Comparative Analysis

### Channel Belt to Active Channel Width Ratio
- **Purpose**: Cross-system comparison of channel belt efficiency
- **Input**: Combined `cross_section_scale` from all five systems
- **Method**: Ratio calculation and comparative visualization
- **Output**: Multi-climate zone comparison plots

## Statistical Methods

### LOWESS Smoothing
- **Application**: Channel gradient profiles
- **Purpose**: Noise reduction in elevation data
- **Parameters**: Configurable smoothing fraction and iterations
- **Reference**: Cleveland (1979); Cleveland and Devlin (1988)

### OLS Regression Analysis
- **Application**: Downstream trend analysis
- **Statistics Generated**:
  - **R²**: Coefficient of determination (trend strength)
  - **p-value**: Statistical significance (threshold < 0.05)
  - **CV**: Coefficient of Variation (variability measure)
- **Scales**: Applied at cross-section, reach, and environmental scales

## Software Requirements

### Core Dependencies
```python
pandas>=1.5.0          # Data manipulation
numpy>=1.21.0           # Numerical computing  
matplotlib>=3.5.0       # Basic plotting
scienceplots>=2.0.0     # Publication-quality plots
scipy>=1.9.0            # Statistical analysis
statsmodels>=0.13.0     # OLS regression
openpyxl>=3.0.0         # Excel file handling
```

### Optional Dependencies
```python
seaborn>=0.11.0         # Enhanced statistical plots
jupyter>=1.0.0          # Interactive notebooks
ipykernel>=6.0.0        # Jupyter kernel support
```

## Usage Instructions

### Interactive Analysis (Recommended)
```bash
# Navigate to system notebooks
cd system-notebooks/

# Launch Jupyter Lab
jupyter lab

# Open and run individual system notebook
# Example: rio_fragua_chorroso_analysis.ipynb
```

### Batch Processing
```bash
# Run individual system analysis
python system-scripts/rio_fragua_chorroso_analysis.py

# Run comparative analysis  
python comparative-analysis/channel_belt_active_ratio_analysis.py
```

### Configuration
```python
# Each system uses its specific config file
from configs.rio_fragua_chorroso_config import *

# Data paths automatically reference ../data/
data_file = f"../data/{SYSTEM_NAME}_analysis_data.xlsx"
```

## Validation and Quality Control

### Data Validation
- **Cross-system consistency**: verification between all five systems
- **Cross-scale consistency**: Verification between system/domain/reach scales

### Reproducibility
- **Standardised methodology**: Identical analysis across all systems
- **Configuration management**: System-specific parameters documented
- **Version control**: All analysis steps tracked and reproducible

## Output Standards

### Figures
- **Format**: SVG for publication quality
- **Style**: SciencePlots with Paul Tol colorblind-friendly palette
- **Resolution**: 300 DPI when exported to raster formats
- **Consistency**: Standardized axis labels, legends, and formatting

### Statistical Tables
- **Format**: Excel with multiple sheets for different analyses
- **Precision**: Consistent decimal places for statistical measures
- **Documentation**: Metadata and units clearly specified

## Applications

This analysis framework supports:
- **Climate-based comparisons**: Systematic analysis across five climate zones
- **Multi-scale understanding**: System, domain, and reach-scale patterns
- **Statistical rigor**: OLS regression with significance testing
- **Reproducible research**: Standardised methodology and documentation
- **Publication quality**: Professional visualisation and data presentation

## References

**Statistical Methods:**
- Cleveland, W.S. (1979) Robust locally weighted regression and smoothing scatterplots. *Journal of the American Statistical Association*, 74(368), 829-836.
- Cleveland, W.S. and Devlin, S.J. (1988) Locally weighted regression: an approach to regression analysis by local fitting. *Journal of the American Statistical Association*, 83(403), 596-610.

**Visualisation:**
- Garrett, N. (2021) SciencePlots: Publication-ready scientific figures. Available at: https://github.com/garrettj403/SciencePlots
- Tol, P. (2021) Colour Schemes. SRON Technical Note. Available at: https://personal.sron.nl/~pault/
