"""
Configuration template for DFS analysis
Reflects the multi-scale measurement and analysis approach
"""

# System identification
SYSTEM_NAME = "System Name"
SYSTEM_ID = "system_id"  
CLIMATE_TYPE = "climate_zone" # e.g., "tropical", "polar", "continental", "subtropical", "dryland"
LOCATION = "Country/Region"

# Data file paths
DATA_ROOT = "/path/to/data/"
SATELLITE_IMAGE = "sentinel2_image.tif"
CHANNEL_CENTERLINE = "centerline.shp" 
ELEVATION_DEM = "elevation.tif"
DIGITISED_FEATURES = "channel_belt_active_bars.shp"

# =============================================================================
# SYSTEM GEOMETRY
# =============================================================================
# Coordinates in decimal degrees (WGS84)
APEX_COORDINATES = (lat, lon)  # upstream apex point
TOE_COORDINATES = (lat, lon)   # downstream toe point
SYSTEM_LENGTH_KM = 0.0         # total system length
POINT_SPACING_M = 100          # distance between measurement points along centerlines

# Analysis parameters
APEX_COORDINATES = (lat, lon)  # decimal degrees 
TOE_COORDINATES = (lat, lon)   # decimal degrees
SYSTEM_LENGTH_KM = 0.0
POINT_SPACING_M = 100  # distance between measurement points

# Multi-scale analysis parameters
CROSS_SECTION_INTERVAL = 5.0  # % of system length for width measurements
REACH_SEGMENT_SIZE = 2.5      # % of cross-section interval, excludes first/last 2.5% leaving 90% analysed
SYSTEM_COVERAGE = 100         # % of entire system areas analysed
DOMAIN_SEGMENT_SIZE = { # Domain boundaries (dividing total length into thirds)
    'PROXIMAL_DOMAIN': '0-33.3%',
    'MEDIAL_DOMAIN': '33.3-66.7%', 
    'DISTAL_DOMAIN': '66.7-100%'
}

# Analysis scales
SCALES = {
    'system': 'entire_system_analysis',
    'domain': ['proximal', 'medial', 'distal'],  # dividing total length into thirds
    'cross_section': 'every_5_percent_downstream',  # measured in km for trend analysis
    'reach': 'continuous_2.5_percent_segments'  # 90% coverage, excludes first/last 2.5%
}

# Cross-section scale measurements (km)
CROSS_SECTION_MEASUREMENTS = {
    'channel_belt_width_km': True,
    'active_channel_width_km': True,  # wetted channel or dry riverbed
    'channel_belt_active_ratio': True,
    'spacing_interval': 5.0  # % of system length
}

# Environmental area analysis - area measurements (km²) calculated at system, domain, and reach scales
ENVIRONMENTAL_TYPES = {
    'wetted_channel': True,      # active flowing channels
    'dry_riverbed': False,       # True only for Unnamed Iranian DFS
    'vegetated_bars': True,      # vegetation-covered bars and islands
    'unvegetated_bars': True,    # bare sediment bars
    'bar_complex': True          # combined vegetated + unvegetated bars
}

# Analysis workflows
ANALYSIS_NOTEBOOKS = {
    'main_analysis': f"{SYSTEM_ID}_dfs_analysis.ipynb",
    'database_analysis': "dfs_database_selection.ipynb"  # separate notebook
}

# Output settings
OUTPUT_FOLDER = f"results/{SYSTEM_ID}/"
FIGURE_DPI = 300
EXCEL_OUTPUT = True
GRADIENT_ANALYSIS = True  # from channel profile extraction
