# Distributive Fluvial Systems Channel Analysis

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--7605--9285-brightgreen.svg)](https://orcid.org/0000-0001-7605-9285)
![GitHub last commit](https://img.shields.io/github/last-commit/kwetishedanjuma/dfs-channel-analysis.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/kwetishedanjuma/dfs-channel-analysis.svg)
![GitHub issues](https://img.shields.io/github/issues/kwetishedanjuma/dfs-channel-analysis.svg)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19319578.svg)](https://doi.org/10.5281/zenodo.19319578)

## Overview

This repository contains the complete analytical workflow for studying channel geometry and environmental distributions in distributive fluvial systems (DFSs) across five major climate zones. The research employs manual digitisation techniques with ArcGIS Pro combined with multi-scale statistical analysis to characterise downstream trends in DFS morphology.

## Study Systems

Analysis of five representative DFS across different climate zones:

| System ID | System Name | Climate Zone | Length (km) | Location | 
|-----------|------|--------------|-------------|----------|
| Colombia06 | Río Fragua Chorroso | Tropical | 30.0 | Colombia |
| Alaska04 | Canning | Polar | 36.9 | Alaska, USA |
| Alaska13 | Nabesna | Continental | 35.4 | Alaska, USA |
| India13 | Brahmaputra | Subtropical | 43.3 | India|
| Iran21 | Unnamed| Drylands | 30.9 | Iran |

## Methodology

### Multi-Scale Analysis Framework
- **System Scale**: Entire DFS analysis (30-43 km length)
- **Domain Scale**: Proximal (0-33.3%), Medial (33.3-66.7%), Distal (66.7-100%) divided equally into thirds
- **Cross-Section Scale**: Transverse measurements every 5% of system length
- **Reach Scale**: Continuous 2.5% segments with 90% system coverage

### Data Sources
- **Satellite Imagery**: Sentinel-2 Surface Reflectance (cloud cover <10%)
- **Elevation Data**: SRTM (30m) and ArcticDEM (2m) via Google Earth Engine
- **Manual Digitisation**: ArcGIS Pro for channel belt and environmental types (e.g., channel belt, wetted channel/dry riverbed, vegetated and unvegetated bars, bar complex) mapping

### Statistical Analysis
- **Trend Analysis**: Ordinary Least Squares (OLS) regression
- **Profile Smoothing**: LOWESS regression for noise reduction
- **Significance Testing**: p < 0.05 threshold
- **Variability Assessment**: Coefficient of Variation (CV)

## Repository Structure

```
dfs-channel-analysis/
├── README.md                  # Project documentation (this file)
├── LICENSE                    # CC-BY-4.0 License
├── requirements.txt           # Python dependencies
├── .gitignore                 # Version control exclusions
│
├── code/                      # Analysis code and workflows
│   ├── arcgis-tools/          # ArcGIS Pro tools for manual digitisation
│   ├── config/                # System-specific configuration and parameters
│   ├── dfs-database-analysis/ # Site selection and database analysis scripts
│   ├── google-earth-engine/   # Data acquisition utilities (e.g., GEE scripts)
│   └── statistical-analysis/  # Python analysis pipeline and plotting
│
├── data/                      # Input datasets (NOT tracked in git; use .gitignore)
│   ├── README.md              # Description of data folder and its contents
│   ├── .gitkeep               # Keeps empty folders in git
│   ├── hartley_et_al_modern_dfs.xlsx         # Modern DFS database
│   ├── Global_DFS_database.kmz               # Spatial visualisation file
│   ├── rio_fragua_chorroso_dfs_analysis_data.xlsx      # System-specific analysis data
│   ├── canning_dfs_analysis_data.xlsx             # System-specific analysis data
│   ├── nabesna_dfs_analysis_data.xlsx             # System-specific analysis data
│   ├── brahmaputra_dfs_analysis_data.xlsx         # System-specific analysis data
│   └── unnamed_iranian_dfs_analysis_data.xlsx       # System-specific analysis data
│
└── results/                   # Analysis outputs (NOT tracked in git; use .gitignore)
    ├── figures/               # Publication-quality plots and figures
    ├── tables/                # Statistical summaries and CSVs
    └── system-outputs/        # Individual system-level results
```

> **Note:**  
> - All large or proprietary data are NOT tracked by git and must be included in your `.gitignore` file.
> - For collaboration, provide metadata or download scripts for data acquisition when possible.

## Quick Start

### 1. Environment Setup
```bash
# Clone repository
git clone https://github.com/kwetishedanjuma/dfs-channel-analysis.git
cd dfs-channel-analysis

# Create Python environment
conda create -n dfs-analysis python=3.8
conda activate dfs-analysis

# Install dependencies
pip install -r requirements.txt
```

### 2. Data Acquisition
1. **Satellite Imagery**: Run Google Earth Engine scripts for complete coverage
2. **Elevation Data**: Download SRTM/ArcticDEM using provided utilities
3. **Manual Digitisation**: Use ArcGIS Pro tools for channel feature mapping

### 3. Analysis Workflow
1. **Site Selection**: Run database analysis to validate system selection
2. **Profile Extraction**: Extract elevation profiles using ArcGIS tools
3. **Statistical Analysis**: Process multi-scale (system, domain, cross-section and reach scales) measurements and trends
4. **Visualisation**: Generate publication-quality figures

## Key Features

- ✅ **Systematic Multi-Scale Analysis** - Consistent methodology across all systems
- ✅ **Climate Zone Representation** - Five major climate zones covered
- ✅ **Reproducible Workflow** - Complete documentation and code
- ✅ **Publication Quality** - Scientific visualisation with colourblind-friendly palettes from Paul Tol's Notes
- ✅ **Manual Digitisation Focus** - High-precision feature mapping without tiny slivers or gaps between polygons 
- ✅ **Statistical Rigor** - OLS regression with significance testing

## Software Requirements

### Core Analysis
- Python 3.8+ with scientific packages (pandas, numpy, matplotlib, scipy)
- Jupyter Notebook for interactive analysis
- SciencePlots for publication-quality visualisation

### Geospatial Processing
- ArcGIS Pro with Spatial Analyst extension
- Google Earth Engine account (JavaScript API)

### Data Formats
- Input: Sentinel-2 GeoTIFF, SRTM/ArcticDEM, ESRI Shapefiles
- Output: Excel tables, PNG/SVG figures, vector datasets

## Results and Applications

This methodology enables:
- **Cross-Climate Comparison**: Systematic analysis across climate zones
- **Downstream Trend Identification**: Statistical characterization of morphological changes
- **Environmental Quantification**: Precise measurement of channel belt components
- **Reproducible Research**: Complete workflow for similar studies

## Citation

If you use this code, workflow, or methodology in your research, please cite:

```
Danjuma, K.J., Owen, A., Dalton, T., Williams, R., & Boothroyd, R. (2026).
Quantitative analysis of channel characteristics of distributive fluvial systems.
Sedimentology. https://doi.org/10.1111/sed.70105

Dataset:
Danjuma, K.J. (2025). Quantitative analysis of channel characteristics of distributive fluvial systems: supporting dataset.
Zenodo. Version 1.0. https://doi.org/10.5281/zenodo.XXXXXXX
```

## License

This project is licensed under the LICENSE-CC-BY-4.0 License - see the [LICENSE-CC-BY](LICENSE-CC-BY) file for details.

## Acknowledgments

- Sentinel‑2 imagery courtesy of the ESA Copernicus Programme  
- SRTM data courtesy of NASA/USGS  
- ArcticDEM courtesy of the Polar Geospatial Centre  
- Modern DFS database from Hartley et al. (2010):

  Hartley, A.J., Weissmann, G.S., Nichols, G.J. & Warwick, G.L. (2010).  
  *Large Distributive Fluvial Systems: Characteristics, Distribution, and Controls on Development.*  
  Journal of Sedimentary Research, 80(2), 167–183. https://doi.org/10.2110/jsr.2010.016

## Contact

**Author**: Kwetishe Joro Danjuma  
**Email**: k.danjuma@outlook.com  
**Institution**: University of Glasgow, UK  
**ORCID**: https://orcid.org/0000-0001-7605-9285

---

*This repository supports systematic analysis of distributive fluvial systems using manual digitisation in ArcGIS Pro and multi-scale statistical approaches using Python and statistical model (e.g., Regression analysis).*
