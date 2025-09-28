## Data Acquisition Workflow

### 1. Download Satellite Imagery (USGS EarthExplorer)
- For each system, use the apex and toe latitude/longitude (see tables below) to define the ROI bounding box.
- Download Sentinel-2, SRTM, and/or ArcticDEM imagery for the region and dates of interest.
- Example:  
  - **Río Fragua Chorroso**:  
    - Apex: 01°19'54.20"N, 75°59'01.07"W  
    - Toe: 01°11'19.58"N, 75°45'21.68"W  
  - (repeat for each system...)

### 2. Digitise Channel Belt
- Open the downloaded imagery in ArcGIS Pro or QGIS.
- Digitise the channel belt and export as `channelBelt.shp`.

### 3. Download Matching Imagery in GEE
- Use the provided [gee_download_roi.js](../code/google-earth-engine/gee_download_roi.js) script in the GEE Code Editor.
- Upload `channelBelt.shp` to your GEE assets and use it as the ROI for image export.
- Select Sentinel-2 or other imagery for the same date and area as your digitisation.

### 4. Example GEE script snippet

```javascript
// gee_download_roi.js
// Import your uploaded channelBelt shapefile as an asset
var channelBelt = ee.FeatureCollection('users/your_username/channelBelt');
var roi = channelBelt.geometry();

// Filter Sentinel-2 imagery for your date and ROI
var s2 = ee.ImageCollection('COPERNICUS/S2')
  .filterBounds(roi)
  .filterDate('2022-07-01', '2022-07-31')
  .filterMetadata('CLOUDY_PIXEL_PERCENTAGE', 'less_than', 10);

// Select the least cloudy image
var image = s2.sort('CLOUDY_PIXEL_PERCENTAGE').first();
Map.centerObject(roi, 10);
Map.addLayer(image, {bands: ['B4','B3','B2'], min:0, max:3000}, 'RGB');

// Export
Export.image.toDrive({
  image: image.clip(roi),
  description: 'Sentinel2_ROI',
  region: roi,
  scale: 10,
  maxPixels: 1e10
});
```

### 5. Study System Apex/Toe Coordinates

| System                   | Location         | Apex (lat, lon)                | Toe (lat, lon)                  | Climate       | Length (km) | Tectonic Setting |
|--------------------------|------------------|--------------------------------|---------------------------------|--------------|-------------|------------------|
| **Río Fragua Chorroso DFS**  | Colombia         | 01°19'54.20"N, 75°59'01.07"W   | 01°11'19.58"N, 75°45'21.68"W    | Tropical     | 30.0        | Foreland         |
| **Canning DFS**        | Alaska, USA      | 70°10'46.09"N, 146°33'33.23"W  | 69°51'02.62"N, 146°27'40.20"W   | Polar        | 36.9        | Foreland         |
| **Nabesna DFS**        | Alaska, USA      | 63°03'15.43"N, 141°57'14.71"W  | 62°47'31.90"N, 142°10'13.80"W   | Continental  | 35.4        | Foreland         |
| **Brahmaputra DFS**    | India            | 28°04'11.65"N, 95°21'16.33"E   | 27°41'45.41"N, 95°16'50.47"E    | Subtropical  | 43.3        | Foreland         |
| **Unnamed Iranian DFS**  | Iran             | 31°58'00.34"N, 58°24'04.15"E   | 31°46'15.03"N, 58°10'15.16"E    | Drylands     | 30.9        | Foreland         |

> **Note:** Coordinates are in degrees, minutes, and seconds (DMS).  
> For use in most GIS/GEE tools, convert to decimal degrees if necessary.

---

### In your `code/google-earth-engine/` folder

- Add your GEE script(s) (e.g., `gee_download_roi.js`)
- README with instructions, example asset import, and parameter customisation.

---

**Summary:**  
Yes, this approach is standard and will make your workflow fully reproducible and open, while keeping your repository lightweight.
