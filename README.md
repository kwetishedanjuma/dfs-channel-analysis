# Distributive Fluvial Systems Channel Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

This repository contains the complete analytical workflow for studying channel geometry and environmental distributions in distributive fluvial systems (DFSs) across five major climate zones. The research employs manual digitisation techniques with ArcGIS Pro combined with multi-scale statistical analysis to characterise downstream trends in DFS morphology.

## Study Systems

Analysis of five representative DFS across different climate zones:

| System ID | Name | Climate Zone | Length (km) | Location |
|-----------|------|--------------|-------------|----------|
| colombia06 | Río Fragua Chorroso | Tropical | 30.0 | Colombia |
| alaska04 | Canning River | Polar | 36.9 | Alaska, USA |
| alaska13 | Nabesna River | Continental | 35.4 | Alaska, USA |
| india13 | Brahmaputra River | Subtropical | 43.3 | India|
| iran21 | Unnamed Iranian DFS | Drylands | 30.9 | Iran |

## Methodology

### Multi-Scale Analysis Framework
- **System Scale**: Entire DFS analysis (30-43 km length)
- **Domain Scale**: Proximal (0-33.3%), Medial (33.3-66.7%), Distal (66.7-100%)
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
├── README.md                    # This file
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
├── .gitignore                   # Version control exclusions
│
├── code/                        # Analysis code and workflows
│   ├── arcgis-tools/           # ArcGIS Pro tools for manual digitization
│   ├── config/                 # System-specific configuration files
│   ├── dfs-database-analysis/  # Site selection analysis
│   ├── google-earth-engine/    # Data acquisition utilities
│   └── statistical-analysis/   # Python analysis pipeline
│
├── data/                       # Input datasets (not tracked in git)
│   ├── satellite-imagery/     # Sentinel-2 imagery
│   ├── elevation/             # SRTM and ArcticDEM data
│   └── vector-data/           # Digitized channel features
│
└── results/                    # Analysis outputs (not tracked in git)
    ├── figures/               # Publication-quality plots
    ├── tables/                # Statistical summaries
    └── system-outputs/        # Individual system results
```

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
4. **Visualization**: Generate publication-quality figures

## Key Features

- ✅ **Systematic Multi-Scale Analysis** - Consistent methodology across all systems
- ✅ **Climate Zone Representation** - Five major climate zones covered
- ✅ **Reproducible Workflow** - Complete documentation and code
- ✅ **Publication Quality** - Scientific visualisation with colorblind-friendly palettes from paul Tol's Notes
- ✅ **Manual Digitisation Focus** - High-precision feature mapping without tiny slivers or gaps between polygons 
- ✅ **Statistical Rigor** - OLS regression with significance testing

## Software Requirements

### Core Analysis
- Python 3.8+ with scientific packages (pandas, numpy, matplotlib, scipy)
- Jupyter Notebook for interactive analysis
- SciencePlots for publication-quality visualization

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

If you use this code or methodology in your research, please cite:

```
[Your Paper Citation Here]
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Sentinel-2 imagery courtesy of ESA Copernicus Programme
- SRTM data courtesy of NASA/USGS
- ArcticDEM courtesy of Polar Geospatial Center
- Modern DFS database from Hartley et al.

## Contact

**Author**: Kwetishe Joro Danjuma  
**Email**: k.danjuma@outlook.com  
**Institution**: University of Glasgow, UK  
**ORCID**: https://orcid.org/0000-0001-7605-9285

---

*This repository supports systematic analysis of distributive fluvial systems using manual digitisation and multi-scale statistical approaches.*
