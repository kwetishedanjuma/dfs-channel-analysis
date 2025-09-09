# Google Earth Engine Data Acquisition Utilities

Standalone JavaScript utilities for acquiring elevation (SRTM/ArcticDEM) and full spatial coverage Sentinel-2 imagery for DFS analysis.

## Purpose

These scripts provide essential data acquisition capabilities for the manual digitisation workflow, ensuring complete spatial coverage and appropriate elevation data for all study systems.

---

## Scripts Included

### [`gee_download_elevation.js`](./gee_download_elevation.js)
- **Purpose**: Download elevation data for channel profile extraction.
- **Data Sources**: SRTM (30m) for most regions, ArcticDEM (2m) for polar/continental systems.
- **Usage**: Substitute `DEM` for SRTM or ArcticDEM within the script as appropriate.
- **How to use**: Open the script for full usage instructions and edit as directed by in-line comments.

### [`gee_download_sentinel-2_fullcoverage.js`](./gee_download_sentinel-2_fullcoverage.js)
- **Purpose**: Download full spatial coverage Sentinel-2 imagery (cloud-masked, single date, matching manual digitisation).
- **Data Source**: Sentinel-2 Surface Reflectance Collection.
- **Usage**: Open the script and edit dates and ROI as described in script comments.

---

## Requirements

- Google Earth Engine account with access to:
  - USGS SRTM Digital Elevation 30m
  - ArcticDEM (for polar and continental systems)
  - Sentinel-2 MSI Surface Reflectance
- Study area boundaries (typically channel belt extent + buffer; use digitised channelBelt.shp)

## Output Specifications

- **Coordinate System**: WGS84 (EPSG:4326) or appropriate UTM zone
- **File Format**: GeoTIFF with proper georeferencing
- **Naming Convention**: `{system_id}_{data_type}_{date}.tif`

---

## Usage Notes

- Scripts are standalone utilities; open each `.js` file for up-to-date examples and usage.
- No automated classification—these support a manual digitisation approach.
- Outputs serve as inputs to ArcGIS-based analysis pipeline.

---

## Study System Apex/Toe Coordinates

| System                   | Location         | Apex (lat, lon)                | Toe (lat, lon)                  | Climate       |
|--------------------------|------------------|--------------------------------|---------------------------------|--------------|
| **Río Fragua Chorroso**  | Colombia         | 01°19'54.20"N, 75°59'01.07"W   | 01°11'19.58"N, 75°45'21.68"W    | Tropical     |
| **Canning River**        | Alaska, USA      | 70°10'46.09"N, 146°33'33.23"W  | 69°51'02.62"N, 146°27'40.20"W   | Polar        |
| **Nabesna River**        | Alaska, USA      | 63°03'15.43"N, 141°57'14.71"W  | 62°47'31.90"N, 142°10'13.80"W   | Continental  |
| **Brahmaputra River**    | India            | 28°04'11.65"N, 95°21'16.33"E   | 27°41'45.41"N, 95°16'50.47"E    | Subtropical  |
| **Unnamed Iranian DFS**  | Iran             | 31°58'00.34"N, 58°24'04.15"E   | 31°46'15.03"N, 58°10'15.16"E    | Drylands     |

> **Note:** Coordinates are in degrees, minutes, and seconds (DMS).  
> For use in most GIS/GEE tools, convert to decimal degrees if necessary.

---

For more details or workflow instructions, see [../docs/data_acquisition.md](../../docs/data_acquisition.md).
