// GEE script for exporting SRTM or ArcticDEM elevation data for a study area.
// NOTE: Substitute either SRTM or ArcticDEM as DEM source for your system.
// Replace "geometry" with your channel belt shapefile or ROI asset.

Map.setCenter({lon: -142.171, lat: 62.792, zoom: 7 });
Map.setOptions('SATELLITE');

// Import study area as FeatureCollection
var studyArea = ee.FeatureCollection(geometry);

// --- Substitute DEM as appropriate ---
// var DEM = ee.Image("USGS/SRTMGL1_003"); // SRTM 30m
// var DEM = ee.Image("UMN/PGC/ArcticDEM/V3/2m_mosaic"); // ArcticDEM 2m
// -------------------------------------
var DEM = ee.Image("USGS/SRTMGL1_003"); // Default to SRTM (edit as needed)

print('DEM Elevation Data:', DEM);

var palettes = require('users/gena/packages:palettes');
var elevation_palette = palettes.crameri.batlow[50];

Map.addLayer(studyArea, {palette: elevation_palette}, 'Study Area');
Map.addLayer(DEM, {min: 0, max: 1000, palette: elevation_palette}, 'DEM elevation');

// Export the DEM
Export.image.toDrive({
  image: DEM,
  description: 'System_ElevationDEM',
  region: studyArea,
  scale: 30, // Use 2 for ArcticDEM, 30 for SRTM
  fileFormat: 'GeoTIFF',
  folder: 'ElevationData',
  maxPixels: 1e13,
});
