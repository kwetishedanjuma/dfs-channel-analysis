# Google Earth Engine Data Acquisition Utilities

Standalone JavaScript utilities for acquiring elevation and satellite imagery data for DFS analysis.

## Purpose
These scripts provide essential data acquisition capabilities for the manual digitisation workflow, ensuring complete spatial coverage and appropriate elevation data for all study systems.

## Scripts Included

### `gee_elevation_download.js`
- **Purpose**: Download elevation data for channel profile extraction
- **Data Sources**: SRTM (30m resolution), ArcticDEM (2m resolution)
- **Output Format**: GeoTIFF
- **Usage**: Required for all systems - provides elevation data for ArcGIS profile analysis

### `gee_sentinel2_complete_coverage.js`
- **Purpose**: Ensure complete Sentinel-2 image coverage
- **Data Source**: Sentinel-2 Surface Reflectance Collection
- **Output Format**: GeoTIFF (RGB and NIR bands)
- **Usage**: When standard tile downloads lack full spatial coverage (e.g., Brahmaputra DFS)
- **Filters**: Cloud cover <10%, single date per system

## Requirements
- Google Earth Engine account with access to:
  - USGS SRTM Digital Elevation 30m
  - Arctic DEM (for polar and continental systems)
  - Sentinel-2 MSI Surface Reflectance
- Study area boundaries (typically channel belt extent + buffer)

## Workflow Integration
1. **Define study area**: Use manually digitised channel belt boundaries
2. **Download elevation data**: Run elevation script for profile extraction
3. **Download imagery**: Run complete coverage script if needed
4. **Import to ArcGIS**: Use outputs in manual digitisation workflow

## Output Specifications
- **Coordinate System**: WGS84 (EPSG:4326) or appropriate UTM zone
- **File Format**: GeoTIFF with proper georeferencing
- **Naming Convention**: `{system_id}_{data_type}_{date}.tif`

## Usage Notes
- Scripts are designed as standalone utilities
- No automated classification - supports manual digitisation approach only
- Outputs serve as inputs to ArcGIS-based analysis pipeline
