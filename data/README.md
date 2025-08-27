# Data Directory

This directory contains input datasets for DFS channel analysis. **Note**: Data files are not tracked in git due to size and licensing restrictions.

## Directory Structure

```
data/
├── README.md                           # This file
├── .gitkeep                           # Keeps empty folders in git
│
├── satellite-imagery/                 # Sentinel-2 imagery
│   ├── rio_fragua_chorroso_sentinel2.tif      # Tropical system (Colombia)
│   ├── canning_river_sentinel2.tif            # Polar system (Alaska)
│   ├── nabesna_river_sentinel2.tif            # Continental system (Alaska)
│   ├── brahmaputra_river_sentinel2.tif        # Subtropical system (India)
│   └── unnamed_iranian_dfs_sentinel2.tif      # Drylands system (Iran)
│
├── elevation/                         # Digital elevation models
│   ├── srtm/                         # SRTM 30m data
│   │   ├── rio_fragua_chorroso_srtm.tif
│   │   ├── canning_river_srtm.tif
│   │   ├── nabesna_river_srtm.tif
│   │   ├── brahmaputra_river_srtm.tif
│   │   └── unnamed_iranian_dfs_srtm.tif
│   └── arcticdem/                     # ArcticDEM 2m data (Alaska systems)
│       ├── canning_river_arcticdem.tif
│       └── nabesna_river_arcticdem.tif
│
├── vector-data/                       # Digitized features
│   ├── centerlines/                   # Channel centerlines
│   │   ├── rio_fragua_chorroso_centerline.shp
│   │   ├── canning_river_centerline.shp
│   │   ├── nabesna_river_centerline.shp
│   │   ├── brahmaputra_river_centerline.shp
│   │   └── unnamed_iranian_dfs_centerline.shp
│   ├── channel-belts/                 # Channel belt boundaries
│   │   ├── rio_fragua_chorroso_channel_belt.shp
│   │   ├── canning_river_channel_belt.shp
│   │   ├── nabesna_river_channel_belt.shp
│   │   ├── brahmaputra_river_channel_belt.shp
│   │   └── unnamed_iranian_dfs_channel_belt.shp
│   └── environments/                  # Environmental features
│       ├── rio_fragua_chorroso_environments.shp
│       ├── canning_river_environments.shp
│       ├── nabesna_river_environments.shp
│       ├── brahmaputra_river_environments.shp
│       └── unnamed_iranian_dfs_environments.shp
│
├── reference-data/                    # External datasets
│   ├── hartley_et_al_modern_dfs.xlsx # Modern DFS database
│   └── study_system_coordinates.csv   # System apex/toe coordinates
│
└── processed/                         # Intermediate processing files
    ├── profile-data/                  # Extracted elevation profiles
    ├── measurements/                  # Cross-section measurements
    └── statistics/                    # Calculated metrics
```

## Data Sources

- **Global_DFS_database.kmz**  
  Google Earth KMZ file associated with:  
  Hartley, A.J., Weissmann, G.S., Nichols, G.J., Warwick, G.L. (2010).  
  "Large distributive fluvial systems: characteristics, distribution, and controls on development."  
  *Journal of Sedimentary Research*, 80(2), 167–183.  
  This file contains locations (apex and toe coordinates) of documented distributive fluvial systems.  
  You can load this file in Google Earth or compatible GIS software to visualize system locations.

### How to Use

- Open `Global_DFS_database.kmz` in Google Earth or GIS software.
- Use the coordinate reference system (CRS) for apex and toe to locate each distributive system.
- Once you identify a system of interest, download corresponding satellite imagery from USGS EarthExplorer, Copernicus Open Access Hub, or other archives.
- This workflow allows you to combine published system locations with up-to-date remote sensing data for further analysis.

- **hartley_et_al_modern_dfs.xlsx**  
  Associated with:  
  Hartley, A.J., Weissmann, G.S., Nichols, G.J., Warwick, G.L. (2010).  
  "Large distributive fluvial systems: characteristics, distribution, and controls on development."  
  *Journal of Sedimentary Research*, 80(2), 167–183. SEPM Society for Sedimentary Geology.

  

## Data Acquisition

### Satellite Imagery
- **Source**: Sentinel-2 Surface Reflectance Collection
- **Platform**: Google Earth Engine
- **Script**: `code/google-earth-engine/gee_sentinel2_complete_coverage.js`
- **Criteria**: Cloud cover <10%, single date per system
- **Format**: GeoTIFF with all bands

### Elevation Data
- **SRTM**: 30m resolution, global coverage
- **ArcticDEM**: 2m resolution, Alaska systems only
- **Platform**: Google Earth Engine
- **Script**: `code/google-earth-engine/gee_elevation_download.js`
- **Format**: GeoTIFF, WGS84 projection

### Vector Data
- **Method**: Manual digitization in ArcGIS Pro
- **Features**: Centerlines, channel belts, environmental polygons
- **Precision**: Sub-pixel accuracy with expert interpretation
- **Format**: ESRI Shapefiles with attribute tables

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
- **Vector**: Quality-controlled through systematic digitization protocols

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
4. **Perform digitization**: Follow ArcGIS workflow documentation
5. **Validate data**: Check completeness and quality before analysis

## Support

For questions about data acquisition or processing, please refer to:
- Individual folder README files
- Code documentation in respective analysis scripts
- Repository issues for technical problems
