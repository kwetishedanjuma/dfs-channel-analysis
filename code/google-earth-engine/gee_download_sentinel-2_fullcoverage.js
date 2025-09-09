// GEE script for exporting full spatial coverage Sentinel-2 imagery for a study area
// Replace "ROI" with your channel belt shapefile or manual bounding box.

function maskS2Clouds(image) {
  var qa = image.select('QA60');
  var cloudBitMask = 1 << 10;
  var cirrusBitMask = 1 << 11;
  var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
      .and(qa.bitwiseAnd(cirrusBitMask).eq(0));
  return image.updateMask(mask).divide(10000)
              .copyProperties(image, ["system:time_start"]);
}

// Load and filter Sentinel-2 images
var S2Image = ee.ImageCollection('COPERNICUS/S2_SR')
    .filterDate('2021-12-01', '2021-12-31') // <-- Edit date range as needed
    .filterBounds(ROI)
    .filterMetadata('CLOUDY_PIXEL_PERCENTAGE', 'less_than', 20)
    .map(maskS2Clouds);

var medianComposite = S2Image.median();

Map.setOptions('SATELLITE');
Map.centerObject(ROI);

Map.addLayer(medianComposite, {min:0.0, max:0.3, bands:['B4', 'B3', 'B2']}, 'Sentinel-2 True Colour');

Export.image.toDrive({
  image: medianComposite,
  description: 'Sentinel2_FullCoverage',
  region: ROI,
  scale: 10,
  fileFormat: 'GeoTIFF',
  folder: 'Sentinel2_Data',
  maxPixels: 1e12
});
