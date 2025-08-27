# Global DFS Database Analysis

Analysis of the global distributive fluvial systems database (Hartley et al. 2010) for systematic study site selection across multiple climatic zones.

## Database Overview

- **Total systems**: 415 DFSs globally
- **Radial distances**: 30-704 km (mean: 86.5 km, median: 52.4 km)
- **Analysis period**: Site selection for multi-climatic DFS study
- **Geographic coverage**: Global distribution across all major continents

## Categorisation Framework

The Hartley et al. database organises DFSs using two primary classification schemes:

### Tectonic Settings (5 categories)
- Compressional
- Cratonic  
- Extensional
- Foreland (54% of database - prioritised)
- Strike-slip

### Climatic Regimes (5 categories)
- Continental
- Drylands
- Polar
- Subtropical  
- Tropical

## Selection Criteria

Systematic framework applied to identify representative study systems:

### Primary Filters
- **Size range**: 30-70 km radial distance (median size representation)
- **Tectonic focus**: Foreland basin environments (dominant setting)
- **Climate diversity**: Representation across all five climatic regimes
- **Data quality**: Minimal anthropogenic modifications

### Data Quality Requirements
- **Imagery availability**: Cloud-free Sentinel-2 coverage
- **Anthropogenic impact**: Minimal human modifications to natural channel patterns
- **Elevation data**: SRTM/ArcticDEM coverage for profile extraction
- **Temporal consistency**: Single-date imagery for consistent analysis

## Selected Systems

Final selection of five representative systems across climate zones:

| System | Location | Climate | Length (km) | Tectonic Setting |
|--------|----------|---------|-------------|------------------|
| **Río Fragua Chorroso** | Colombia | Tropical | 30.0 | Foreland |
| **Canning River** | Alaska, USA | Polar | 36.9 | Foreland |
| **Nabesna River** | Alaska, USA | Continental | 35.4 | Foreland |
| **Brahmaputra River** | India/Bangladesh | Subtropical | 43.3 | Foreland |
| **Unnamed Iranian DFS** | Iran | Drylands | 30.9 | Foreland |

## Data Sources

All datasets are stored in the `../data` folder:

### Primary Database
**`hartley_et_al_modern_dfs.xlsx`**
- Comprehensive global DFS compilation
- Statistical and morphometric data for 415 systems
- Associated with: Hartley, A.J., Weissmann, G.S., Nichols, G.J. and Warwick, G.L. (2010) 'Large distributive fluvial systems: characteristics, distribution, and controls on development', *Journal of Sedimentary Research*, 80(2), pp.167-183.

### Spatial Data
**`Global_DFS_database.kmz`**
- Google Earth KMZ file for spatial visualization
- Geographic locations of all 415 distributive fluvial systems
- Compatible with Google Earth Pro and GIS software
- Associated with: Hartley et al. (2010) - same reference as above

## Analysis Files

Analysis code is provided in this folder:

### Interactive Analysis
**`dfs_database_selection.ipynb`**
- Jupyter notebook for exploratory analysis of the Hartley et al. database
- Statistical visualization and site selection validation
- Climate zone and tectonic setting distribution analysis
- Generates publication-quality figures for site selection justification

### Batch Processing
**`dfs_database_analysis.py`**
- Python script version for automated or command-line execution
- Identical analysis to notebook but optimized for batch processing
- Suitable for integration into larger analysis pipelines

## Running the Analysis

### Interactive Exploration
```bash
# Open notebook in JupyterLab
jupyter lab dfs_database_selection.ipynb
```

### Script Execution
```bash
# Run as Python script
python dfs_database_analysis.py
```

### Dependencies
```bash
# Required Python packages
pip install pandas numpy matplotlib scienceplots seaborn
```

## Usage Notes

### Spatial Visualisation
- KMZ file opens in Google Earth Pro for global system overview
- Database provides global context for selected study systems
- Download satellite imagery from USGS EarthExplorer for detailed analysis

### Database Integration
- Excel file contains complete morphometric database
- KMZ file enables automated data acquisition workflows
- Spatial data supports GIS-based analysis and mapping

### Quality Control
- All selected systems validated against original database
- Site selection criteria documented for reproducibility
- Statistical representativeness confirmed across climate zones

## Outputs

Analysis generates the following deliverables:

### Figures
- **Figure 1A**: Tectonic setting distribution across global database
- **Figure 1B**: Climatic regime distribution and study system positions
- **Site selection validation**: Statistical justification plots

### Tables
- **Selection summary**: Chosen systems with key characteristics
- **Database statistics**: Global DFS morphometric summaries
- **Climate representation**: Coverage across all climatic regimes

### Documentation
- **Site selection justification**: Academic rationale for methodology
- **Statistical validation**: Representativeness analysis
- **Quality assessment**: Data quality and completeness metrics

## Applications

This analysis supports:
- **Systematic site selection** for multi-climatic DFS studies
- **Global DFS characterization** using the Hartley et al. database
- **Climate-tectonic framework** for distributive fluvial system analysis
- **Reproducible methodology** for similar comparative studies

## References

**Primary Database:**
Hartley, A.J., Weissmann, G.S., Nichols, G.J. and Warwick, G.L. (2010) 'Large distributive fluvial systems: characteristics, distribution, and controls on development', *Journal of Sedimentary Research*, 80(2), pp.167-183.

**Additional Context:**
- Database represents most comprehensive global compilation of modern DFS
- Selection methodology ensures representative coverage across climate zones
- Analysis supports systematic comparison of DFS morphology and environmental controls
