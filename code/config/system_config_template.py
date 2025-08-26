"""
Configuration template for DFS analysis
Reflects the multi-scale measurement and analysis approach
"""

# SYSTEM IDENTIFICATION
SYSTEM_NAME = "System Name"
SYSTEM_ID = "system_id"  
CLIMATE_TYPE = "climate_zone" # e.g., "tropical", "polar", "continental", "subtropical", "dryland"
LOCATION = "Country/Region"

# DATA FILE PATHS
DATA_ROOT = "/path/to/data/"
SATELLITE_IMAGE = "sentinel2_image.tif"
CHANNEL_CENTERLINE = "centerline.shp" 
ELEVATION_DEM = "elevation.tif"
DIGITISED_FEATURES = "channel_belt_active_bars.shp"

# SYSTEM GEOMETRY - Coordinates in decimal degrees (WGS84)
APEX_COORDINATES = (lat, lon)  # upstream apex point
TOE_COORDINATES = (lat, lon)   # downstream toe point
SYSTEM_LENGTH_KM = 0.0         # total system length
POINT_SPACING_M = 100          # distance between measurement points along centerlines

# MULTI-SCALE ANALYSIS PARAMETERS
CROSS_SECTION_INTERVAL = 5.0  # % of system length for width measurements
REACH_SEGMENT_SIZE = 2.5      # % of cross-section interval, excludes first/last 2.5% leaving 90% analysed
SYSTEM_COVERAGE = 100         # % of entire system areas analysed
DOMAIN_SEGMENT_SIZE = { # Domain boundaries (dividing total length into thirds)
    'PROXIMAL_DOMAIN': '0-33.3%',
    'MEDIAL_DOMAIN': '33.3-66.7%', 
    'DISTAL_DOMAIN': '66.7-100%'
}

# ANALYSIS SCALES
SCALES = {
    'system': 'entire_system_analysis', # whole DFS
    'domain': ['proximal', 'medial', 'distal'],  # dividing total length into thirds
    'cross_section': 'every_5_percent_downstream',  # measured in km for trend analysis
    'reach': 'continuous_2.5_percent_segments'  # 90% coverage, excludes first/last 2.5%
}

# CROSS-SECTION SCALE MEASUREMENTS - data collection parameters
CROSS_SECTION_MEASUREMENTS = { # Measurements taken perpendicular to flow direction at regular intervals
    'channel_belt_width_km': True,                # total width of active channel belt
    'active_channel_width_km': True,              # wetted channel or dry riverbed width
    'channel_belt_active_channel_ratio': True,    # ratio of channel belt to active channel widths ratios
    'spacing_interval': 5.0                       # % of system length between cross-sections
    'units': 'kilometers',                        # measurement units
    'perpendicular_to_flow': True                 # measurements taken across flow direction
}

# ENVIRONMENTAL AREA ANALYSIS - area measurements (km²) calculated at system, domain, and reach scales
ENVIRONMENTAL_TYPES = {
    'wetted_channel': True,      # active flowing channels
    'dry_riverbed': False,       # True only for Unnamed Iranian DFS
    'vegetated_bars': True,      # vegetation-covered bars and islands
    'unvegetated_bars': True,    # bare sediment bars
    'bar_complex': True          # combined vegetated + unvegetated bars
}

# STATISTICAL ANALYSIS PARAMETERS
## Trend analysis settings
TREND_ANALYSIS = {
    'method': 'OLS',                    # Ordinary Least Squares regression for trend analysis
    'significance_level': 0.05,         # p-value threshold for statistical significance
    'coefficient_of_variation': True,   # calculate CV for variability assessment
    'scales': ['system', 'domain', 'reach']  # spatial scales for OLS analysis
}

## Profile smoothing parameters
PROFILE_SMOOTHING = {
    'method': 'LOWESS',                # LOWESS regression (Cleveland 1979; Cleveland and Devlin 1988)
    'frac': 0.3,                       # fraction of data used for smoothing
    'it': 3,                           # number of iterations
    'apply_to_profiles': True          # smooth noise in long profiles
}

## Cross-section trend analysis - how to analyze the measurements
CROSS_SECTION_ANALYSIS = {
    'trend_method': 'OLS',                      # Ordinary Least Squares regression
    'spatial_scales': ['system', 'domain', 'reach'],  # analysis scales
    'assess_downstream_changes': True,          # test for downstream trends
    'significance_level': 0.05,                # p-value threshold
    'coefficient_of_variation': True           # calculate CV for variability assessment
}

# VISUALISATION SETTINGS
PLOTTING = {
    'style': 'science',            # matplotlib style (requires scienceplots)
    'figure_size': (12, 8),        # default figure dimensions
    'dpi': 300,                    # resolution for saved figures
    'color_palette': 'paul_tol',   # Paul Tol's Notes colour palette for colorblind accessibility
    'font_size': 12,               # base font size
    'line_width': 2.0              # default line width
}

# ANALYSIS WORKFLOW NOTEBOOKS
ANALYSIS_NOTEBOOKS = {
    'main_analysis': f"{SYSTEM_ID}_dfs_analysis.ipynb",
    'database_analysis': "dfs_database_selection.ipynb"  # separate comparative notebook
}

# Output settings
OUTPUT_FOLDER = f"results/{SYSTEM_ID}/"
FIGURE_DPI = 300
FIGURE_FORMAT = 'png'           # or 'pdf', 'svg', 'tiff'
EXCEL_OUTPUT = True             # export data tables to Excel
CSV_OUTPUT = True               # export data tables to CSV
SAVE_INTERMEDIATE = False       # save intermediate processing steps

# SYSTEM-SPECIFIC DATA DETAILS
## Five study systems with acquisition details
STUDY_SYSTEMS = {
    'colombia06': {
        'name': 'Río Fragua Chorroso',
        'climate': 'Tropical',
        'length_km': 30.0,
        'apex_coords': (1.332278, -75.983631),  # 01°19'54.20"N, 75°59'01.07"W
        'termination_type': 'Tributary',
        'acquisition_date': '2020-11-09'
    },
    'alaska04': {
        'name': 'Canning',
        'climate': 'Polar', 
        'length_km': 36.9,
        'apex_coords': (69.850728, -146.461167),  # 69°51'02.62"N, 146°27'40.20"W
        'termination_type': 'Marine',
        'acquisition_date': '2021-07-19'
    },
    'alaska13': {
        'name': 'Nabesna',
        'climate': 'Continental',
        'length_km': 35.4, 
        'apex_coords': (62.792194, -142.171167),  # 62°47'31.90"N, 142°10'13.80"W
        'termination_type': 'Axial',
        'acquisition_date': '2019-09-08'
    },
    'india13': {
        'name': 'Brahmaputra',
        'climate': 'Subtropical',
        'length_km': 43.3,
        'apex_coords': (28.069903, 95.354536),  # 28°04'11.65"N, 95°21'16.33"E
        'termination_type': 'Tributary', 
        'acquisition_date': '2020-12-31',
        'special_processing': 'Google Earth Engine workflow for complete coverage'
    },
    'iran21': {
        'name': 'Unnamed Iranian DFS',
        'climate': 'Drylands',
        'length_km': 30.9,
        'apex_coords': (31.966761, 58.401153),  # 31°58'00.34"N, 58°24'04.15"E
        'termination_type': 'Playa',
        'acquisition_date': '2021-10-15',
        'special_note': 'Dry when imaged - uses dry riverbed category instead of wetted channels'
    }
}

# SOFTWARE AND DEPENDENCIES
## Python analysis environment
PYTHON_REQUIREMENTS = {
    'jupyter': 'Jupyter Notebook environment',
    'pandas': 'data manipulation and analysis',
    'numpy': 'numerical computing (Harris et al. 2020)', 
    'matplotlib': 'plotting and visualization (Hunter 2007)',
    'scienceplots': 'colorblind-friendly visualization (Garrett 2021)',
}

# Google Earth Engine data acquisition utilities
GEE_UTILITIES = {
    'elevation_download': {
        'script': 'gee_elevation_download.js',
        'purpose': 'Download elevation data for profile extraction',
        'data_sources': ['SRTM', 'ArcticDEM'],
        'output_format': 'GeoTIFF',
        'resolution': '30m (SRTM), 2m (ArcticDEM)',
        'use_case': 'All systems - required for channel profile analysis'
    },
    'complete_spatial_coverage': {
        'script': 'gee_sentinel2_complete_coverage.js', 
        'purpose': 'Ensure complete Sentinel-2 image coverage',
        'data_source': 'Sentinel-2 Surface Reflectance',
        'output_format': 'GeoTIFF',
        'use_case': 'When standard downloads lack full spatial coverage (e.g., Brahmaputra DFS)',
        'cloud_filter': '<10%',
        'temporal_filter': 'Single date acquisition per system'
    }
}
