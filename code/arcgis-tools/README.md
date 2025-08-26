# ArcGIS Tools

ArcGIS Pro tools for extracting channel geometry and elevation profiles from DFSs.

## Tools Included
- `channel_profile_extraction.py` - Extracts elevation profiles along digitized channel centerlines

## Requirements
- ArcGIS Pro with Spatial Analyst extension
- Python 3.x (included with ArcGIS Pro)
- `Input`: Channel centreline feature class
- `Input`: Digital elevation model (raster)

## Workflow
- Digitise channel centrelines from satellite imagery
- Run profile extraction tool to generate elevation data
- Export results for statistical analysis

## Outputs
- Excel files with distance/elevation data
- PNG elevation profile plots
- Point feature classes with extracted values
