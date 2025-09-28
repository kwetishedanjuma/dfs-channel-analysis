# Results Directory

This directory contains analysis outputs from DFS channel analysis.

> **Note:** Most result files are not tracked in git as they are generated from reproducible code or manual digitisation.  
> For review purposes, representative results may be included here.

---

## Directory Structure

```
results/
├── README.md                       # This file
├── .gitkeep                        # Keeps empty folders in git
│
├── dfs-database-analysis/          # Plots from database/system selection analysis
│   ├── tectonic_setting_main.svg
│   ├── tectonic_setting_zoomed_in.svg
│   ├── climate_basin_main.svg
│   ├── climate_basin_zoomed_in.svg
│   └── ...etc.
│
├── statistical-analysis/           # All figures/tables from system and cross-system analysis
│   ├── rio_fragua_chorroso_channel_gradient.svg
│   ├── rio_fragua_chorroso_cross_section_channel_belt_vs_wetted_channel.svg
│   ├── rio_fragua_chorroso_cross_section_wetted_channel_vs_unveg_vs_veg_bars.svg
│   ├── rio_fragua_chorroso_cross_section_normalised_wetted_channel_vs_unveg_vs_veg_bars.svg
│   ├── canning_river_channel_gradient.svg
│   ├── canning_river_cross_section_channel_belt_vs_wetted_channel.svg
│   ├── canning_river_cross_section_wetted_channel_vs_unveg_vs_veg_bars.svg
│   ├── canning_river_cross_section_normalised_wetted_channel_vs_unveg_vs_veg_bars.svg
│   ├── nabesna_river_channel_gradient.svg
│   ├── nabesna_river_cross_section_channel_belt_vs_wetted_channel.svg
│   ├── nabesna_river_cross_section_wetted_channel_vs_unveg_vs_veg_bars.svg
│   ├── nabesna_river_cross_section_normalised_wetted_channel_vs_unveg_vs_veg_bars.svg
│   ├── brahmaputra_river_channel_gradient.svg
│   ├── brahmaputra_river_cross_section_channel_belt_vs_wetted_channel.svg
│   ├── brahmaputra_river_cross_section_wetted_channel_vs_unveg_vs_veg_bars.svg
│   ├── brahmaputra_river_cross_section_normalised_wetted_channel_vs_unveg_vs_veg_bars.svg
│   ├── unnamed_iranian_dfs_channel_gradient.svg
│   ├── unnamed_iranian_dfs_cross_section_channel_belt_vs_dry_riverbed.svg
│   ├── unnamed_iranian_dfs_cross_section_dry_riverbed_vs_unveg_vs_veg_bars.svg
│   ├── unnamed_iranian_dfs_cross_section_normalised_dry_riverbed_vs_unveg_vs_veg_bars.svg
│   ├── system_scale_environment_vs_area.svg
│   ├── domain_scale_water_area_vs_sediment_area_vs_vegetation_area.svg
│   ├── domain_scale_normalised_water_area_vs_sediment_area_vs_vegetation_area.svg
│   ├── cross_section_ols_analysis_summary.csv
│   ├── reach_scale_ols_analysis_summary.csv
│   └── ...etc.
│
├── gis-mapping/                    # Compressed shapefile archives per system
│   ├── rio_fragua_chorroso_shapefile.zip
│   ├── canning_river_shapefile.zip
│   ├── nabesna_river_shapefile.zip
│   ├── brahmaputra_river_shapefile.zip
│   ├── unnamed_iranian_dfs_shapefile.zip
│   └── ...etc.
```

---

## Output Categories

### Database Analysis Plots
- **Folder:** dfs-database-analysis/
- **Examples:** tectonic_setting_main.svg, climate_basin_zoomed_in.svg

### Statistical Analysis Outputs
- **Folder:** statistical-analysis/
- **Naming:** `[system]_[analysis_type].svg` or `.csv`
- **Examples:** rio_fragua_chorroso_channel_gradient.svg, cross_section_ols_analysis_summary.csv

### GIS Mapping Shapefiles
- **Folder:** gis-mapping/
- **Format:** Each system's shapefiles and associated files are bundled into a single compressed archive (`.zip`)
- **Examples:** rio_fragua_chorroso_shapefile.zip, canning_river_shapefile.zip

---

## File Naming Convention

- **System Names:**
    - `rio_fragua_chorroso` - Río Fragua Chorroso (Tropical, Colombia)
    - `canning_river` - Canning River (Polar, Alaska)
    - `nabesna_river` - Nabesna River (Continental, Alaska)
    - `brahmaputra_river` - Brahmaputra River (Subtropical, India)
    - `unnamed_iranian_dfs` - Unnamed Iranian DFS (Drylands, Iran)
- **Analysis Types:**  
    - `channel_gradient`, `cross_section_channel_belt_vs_wetted_channel`, `cross_section_wetted_channel_vs_unveg_vs_veg_bars`,  
      `cross_section_normalised_wetted_channel_vs_unveg_vs_veg_bars`, `cross_section_channel_belt_vs_dry_riverbed`,  
      `cross_section_dry_riverbed_vs_unveg_vs_veg_bars`, `cross_section_normalised_dry_riverbed_vs_unveg_vs_veg_bars`, etc.
    - Multi-system summaries: `system_scale_environment_vs_area.svg`, etc.

---

## Example Files

```
statistical-analysis/rio_fragua_chorroso_channel_gradient.svg
statistical-analysis/canning_river_cross_section_channel_belt_vs_wetted_channel.svg
statistical-analysis/cross_section_ols_analysis_summary.csv
gis-mapping/brahmaputra_river_shapefile.zip
gis-mapping/unnamed_iranian_dfs_shapefile.zip
dfs-database-analysis/tectonic_setting_zoomed_in.svg
```

---

## Analysis Workflow Outputs

1. **Database Selection Analysis:**  
   - System selection validation  
   - Climate zone and tectonic setting distribution

2. **Profile & Cross-Section Analysis:**  
   - Elevation profiles  
   - Channel belt, wetted channel/dry riverbed, and environmental area measurements  
   - Statistical summaries, OLS regressions

3. **Environmental Analysis:**  
   - Area quantification of wetted channels/dry riverbeds, vegetated/unvegetated bars

4. **Multi-Scale Statistics:**  
   - System-scale, domain-scale, cross-section, and reach-scale outputs

---

## Quality Control

- **Data Validation:**  
  Automated checks, outlier detection, cross-system consistency

- **Figure & Table Standards:**  
  Consistent labels, color palettes, formatting, metadata

---

## Usage Notes

- **Regeneration:**  
  All results can be regenerated by running the complete analysis pipeline:
  ```bash
  jupyter notebook code/statistical-analysis/main_dfs_analysis.ipynb
  ```
- **Dependencies:**  
  Results depend on processed data in `data/` and proper execution of the analysis pipeline.

- **Version Control:**  
  Results are excluded from git tracking (see `.gitignore`).  
  Representative results may be included for review or publication.

---

## Applications

- **Academic Publication:** Figures, tables, and supplementary shapefiles
- **Comparative Analysis:** System and climate comparisons
- **Methodology Validation:** Reproducible workflows and statistical rigor

---

## Support

For questions about result interpretation or regeneration:
- See analysis notebook documentation
- Review code comments for methodology
- Open repository issues for technical support
