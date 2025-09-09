# Google Earth Engine Data Acquisition Utilities

Standalone JavaScript utilities for acquiring elevation and satellite imagery data for DFS analysis.

## Purpose

These scripts provide essential data acquisition capabilities for the manual digitisation workflow, ensuring complete spatial coverage and appropriate elevation data for all study systems.

---

## Scripts Included

### `gee_elevation_download.js`

- **Purpose**: Download elevation data (SRTM 30m, ArcticDEM 2m) for channel profile extraction.
- **Data Sources**: SRTM (30m resolution), ArcticDEM (2m resolution)
- **Output Format**: GeoTIFF
- **Usage**: Required for all systems - provides elevation data for ArcGIS profile analysis

**Sample Usage:**
```javascript
// Set up map view
Map.setCenter({lon: -142.171, lat: 62.792, zoom: 7 });
Map.setOptions('SATELLITE');

// Import channel belt geometry as study area (replace "geometry" with your asset)
var studyArea = ee.FeatureCollection(geometry);

// Print ArcticDEM Image details to the console
print('ArcticDEM Elevation Data at 2m:', ArcticDEM);

var palettes = require('users/gena/packages:palettes');
var elevation_palette = palettes.crameri.batlow[50];

Map.addLayer(studyArea, {min: -50, max: 1000, palette: elevation_palette}, 'Alaska13River');
Map.addLayer(ArcticDEM, {min: -50, max: 1000, palette: elevation_palette}, 'ArcticDEM elevation');

Export.image.toDrive({
  image: ArcticDEM,
  description: 'Alaska13RiverArcticDEM',
  region: studyArea,
  scale: 30,
  fileFormat: 'GeoTIFF',
  folder: 'SRTMArcticDEM Data',
  maxPixels: 1e13,
});
```

### `gee_srtm_download.js`

- **Purpose**: Download SRTM elevation for non-polar regions.
- **Data Source**: USGS SRTM Digital Elevation 30m
- **Output Format**: GeoTIFF
- **Usage**: Required for all systems except those covered by ArcticDEM

**Sample Usage:**
```javascript
Map.setCenter({lon: 95.355, lat: 28.07, zoom: 12 });
Map.setOptions('SATELLITE');
var studyArea = ee.FeatureCollection(geometry);
print('The SRTM Digital Elevation Data at 30m:', SRTM);

var palettes = require('users/gena/packages:palettes');
var elevation_palette = palettes.crameri.batlow[50];

Map.addLayer(studyArea, {min: 0, max: 1000, palette: elevation_palette}, 'India13River');
Map.addLayer(SRTM, {min: 0, max: 1000, palette: elevation_palette}, 'SRTM elevation');

Export.image.toDrive({
  image: SRTM,
  description: 'India13River_v1SRTM',
  region: studyArea,
  scale: 30,
  fileFormat: 'GeoTIFF',
  folder: 'SRTMArcticDEM Data',
  maxPixels: 1e13,
});
```

### `gee_sentinel2_complete_coverage.js`

- **Purpose**: Ensure complete Sentinel-2 image coverage, with cloud masking and date filtering.
- **Data Source**: Sentinel-2 Surface Reflectance Collection
- **Output Format**: GeoTIFF (RGB and NIR bands)
- **Usage**: When standard tile downloads lack full spatial coverage (e.g., Brahmaputra DFS)
- **Filters**: Cloud cover <20%, single date per system

**Sample Usage:**
```javascript
function maskS2Clouds(image) {
  var qa = image.select('QA60');
  var cloudBitMask = 1 << 10;
  var cirrusBitMask = 1 << 11;
  var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
      .and(qa.bitwiseAnd(cirrusBitMask).eq(0));
  return image.updateMask(mask).divide(10000)
              .copyProperties(image, ["system:time_start"]);
}
var S2Image = ee.ImageCollection('COPERNICUS/S2_SR')
    .filterDate('2021-12-01', '2021-12-31')
    .filterBounds(studyArea)
    .filterMetadata('CLOUDY_PIXEL_PERCENTAGE','less_than',20)
    .map(maskS2Clouds);

var medianComposite = S2Image.median();

Map.setOptions('SATELLITE');
Map.centerObject(studyArea);

Map.addLayer(medianComposite, {min:0.0, max:0.3, bands:['B4', 'B3', 'B2']}, 'Sentinel-2 True Colour');

Export.image.toDrive({
  image: medianComposite,
  description: 'Sentinel2_CompleteCoverage',
  region: studyArea,
  scale: 10,
  fileFormat: 'GeoTIFF',
  folder: 'Sentinel2_Data',
  maxPixels: 1e12
});
```

---

## Requirements

- Google Earth Engine account with access to:
  - USGS SRTM Digital Elevation 30m
  - Arctic DEM (for polar and continental systems)
  - Sentinel-2 MSI Surface Reflectance
- Study area boundaries (typically channel belt extent + buffer; use digitised channelBelt.shp)

---

## Workflow Integration

1. **Define study area**: Use manually digitised channel belt boundaries.
2. **Download elevation data**: Run elevation script for profile extraction.
3. **Download imagery**: Run complete coverage script if needed.
4. **Import to ArcGIS**: Use outputs in manual digitisation workflow.

---

## Output Specifications

- **Coordinate System**: WGS84 (EPSG:4326) or appropriate UTM zone
- **File Format**: GeoTIFF with proper georeferencing
- **Naming Convention**: `{system_id}_{data_type}_{date}.tif`

---

## Usage Notes

- Scripts are designed as standalone utilities.
- No automated classification - supports manual digitisation approach only.
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

## How To Use

- Replace `geometry` or `studyArea` with your uploaded `channelBelt` shapefile or bounding box (see coordinates above).
- Use the sample scripts directly in the GEE Code Editor (`https://code.earthengine.google.com/`).
- Adjust export parameters (region, scale, folder, etc.) for your workflow.

See [../docs/data_acquisition.md](../../docs/data_acquisition.md) for the complete workflow and further instructions.
