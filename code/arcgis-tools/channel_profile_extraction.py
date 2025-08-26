"""
Channel Profile Analysis Tool
Created March 2022 

@author: Craig MacDonell
@contributor: Kwetishe Joro Danjuma

This ArcGIS tool extracts elevation profiles along manually digitised channel centrelines for 
distributive fluvial systems (DFSs) analysis. It creates regularly spaced points 
along a centreline, extracts elevation values from a DEM, and generates 
profile plots with associated data exports.

Requirements:
- ArcGIS Pro with Spatial Analyst extension
- Input centreline feature class
- Digital elevation model (raster)
- Projected coordinate system

Outputs:
- Excel file with elevation profile data
- PNG plot of the profile
- Temporary geodatabase with processing results
"""

import sys
import arcpy as ap
from arcpy import env
from arcpy.sa import *
import os
import time
from time import process_time
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import traceback

# Allow overwriting in ArcGIS
ap.env.overwriteOutput = True

def validate_coordinate_system(wkt):
    """
    Validate that the coordinate system is projected (not geographic).
    
    Args:
        wkt (str): Well-known text representation of coordinate system
        
    Returns:
        arcpy.SpatialReference: Validated coordinate system object
        
    Raises:
        ExecuteError: If coordinate system is not projected
    """
    coord_sys = ap.SpatialReference(text=wkt)
    
    if coord_sys.type != "Projected":
        ap.AddError("Projected coordinate system required. Please use a projected coordinate system (e.g., UTM) instead of geographic (lat/lon).")
        sys.exit()
    
    ap.env.outputCoordinateSystem = coord_sys
    ap.AddMessage("Validated projected coordinate system - processing will continue")
    return coord_sys

def create_processing_environment(root_path, site_name):
    """
    Create temporary geodatabase and output folders for processing.
    
    Args:
        root_path (str): Root directory for outputs
        site_name (str): Site name for folder naming
        
    Returns:
        tuple: (temp_gdb_path, output_plot_folder)
    """
    start_time = process_time()
    ap.AddMessage("Creating temporary processing geodatabase and output folder")
    
    # Create temporary geodatabase
    temp_gdb = os.path.join(root_path, 'temp_process.gdb')
    if not ap.Exists(temp_gdb):
        ap.management.CreateFileGDB(root_path, 'temp_process.gdb')
    
    # Create output folder
    output_folder = os.path.join(root_path, f"{site_name}_outputPlotsData")
    if not os.path.isdir(output_folder):
        os.mkdir(output_folder)
    
    elapsed_time = process_time() - start_time
    ap.AddMessage(f"Created processing environment in {elapsed_time:.2f} seconds")
    
    return temp_gdb, output_folder

def validate_and_reproject_line(input_line, line_length_field, coord_sys, temp_gdb, site_name):
    """
    Validate input line and reproject if necessary.
    
    Args:
        input_line (str): Input centreline feature class
        line_length_field (str): Field name for line length
        coord_sys (arcpy.SpatialReference): Target coordinate system
        temp_gdb (str): Temporary geodatabase path
        site_name (str): Site name for output naming
        
    Returns:
        tuple: (processed_line_path, line_length_value)
    """
    start_time = process_time()
    ap.AddMessage("Validating input line and checking projection")
    
    # Check if single feature
    feature_count = int(ap.management.GetCount(input_line)[0])
    if feature_count > 1:
        ap.AddError("Input must be a single line feature. Consider using Dissolve tool first.")
        sys.exit()
    
    # Get line length
    with ap.da.SearchCursor(input_line, 'SHAPE@LENGTH') as cursor:
        for row in cursor:
            line_length = row[0]
            break
    
    # Check projection and reproject if needed
    line_epsg = ap.Describe(input_line).spatialReference.factoryCode
    target_epsg = coord_sys.factoryCode
    
    if line_epsg != target_epsg:
        ap.AddMessage("Reprojecting centreline to match coordinate system")
        reprojected_line = os.path.join(temp_gdb, f"{site_name}_centreline_reprojected")
        ap.management.Project(input_line, reprojected_line, coord_sys)
        
        # Recalculate length in new projection
        geom_cmd = f"{line_length_field} LENGTH"
        ap.management.CalculateGeometryAttributes(reprojected_line, geom_cmd, 
                                                coord_sys.linearUnitName.upper(), 
                                                '', coord_sys)
        
        with ap.da.SearchCursor(reprojected_line, line_length_field) as cursor:
            for row in cursor:
                line_length = row[0]
                break
        
        input_line = reprojected_line
    else:
        ap.AddMessage("Coordinate systems match - no reprojection needed")
    
    elapsed_time = process_time() - start_time
    ap.AddMessage(f"Line validation completed in {elapsed_time:.2f} seconds. Length: {line_length:.2f}m")
    
    return input_line, line_length

def generate_elevation_points(input_line, point_distance, input_raster, temp_gdb):
    """
    Generate points along line and extract elevation values.
    
    Args:
        input_line (str): Input centreline feature class
        point_distance (str): Distance between points (with units)
        input_raster (str): Input elevation raster
        temp_gdb (str): Temporary geodatabase path
        
    Returns:
        str: Path to elevation points feature class
    """
    start_time = process_time()
    
    # Generate regular points along line
    ap.AddMessage("Generating points along centreline")
    regular_points = os.path.join(temp_gdb, 'regular_points')
    ap.GeneratePointsAlongLines_management(
        input_line, regular_points, 'DISTANCE', 
        Distance=point_distance, Include_End_Points='END_POINTS'
    )
    
    # Clean up unnecessary fields
    if ap.ListFields(regular_points, "ORIG_FID"):
        ap.DeleteField_management(regular_points, "ORIG_FID")
    
    point_time = process_time() - start_time
    ap.AddMessage(f"Generated points in {point_time:.2f} seconds")
    
    # Extract elevation values
    ap.AddMessage("Extracting elevation values from raster")
    elevation_points = os.path.join(temp_gdb, 'elevation_points')
    ExtractValuesToPoints(regular_points, input_raster, elevation_points, 
                         "NONE", "VALUE_ONLY")
    
    elapsed_time = process_time() - start_time
    ap.AddMessage(f"Elevation extraction completed in {elapsed_time:.2f} seconds")
    
    return elevation_points

def calculate_distances(elevation_points, point_distance, line_length):
    """
    Calculate cumulative distances along the line for each point.
    
    Args:
        elevation_points (str): Points with elevation values
        point_distance (str): Distance between points (with units)
        line_length (float): Total line length
    """
    start_time = process_time()
    ap.AddMessage("Calculating distances along centreline")
    
    # Add distance field
    ap.management.AddField(elevation_points, "distance_m", "DOUBLE")
    
    # Calculate distances
    distance_interval = float(point_distance.split(' ')[0])
    current_distance = 0
    
    with ap.da.UpdateCursor(elevation_points, 'distance_m') as cursor:
        for row in cursor:
            if current_distance <= line_length:
                row[0] = current_distance
                current_distance += distance_interval
            else:
                row[0] = line_length
            cursor.updateRow(row)
    
    # Rename elevation field for clarity
    ap.AlterField_management(elevation_points, 'RASTERVALU', 'elevation_m', 'Elevation (m)')
    
    elapsed_time = process_time() - start_time
    ap.AddMessage(f"Distance calculations completed in {elapsed_time:.2f} seconds")

def export_and_plot_data(elevation_points, output_folder, site_name, x_label, y_label, plot_title):
    """
    Export data to Excel and create elevation profile plot.
    
    Args:
        elevation_points (str): Points with elevation and distance data
        output_folder (str): Output folder path
        site_name (str): Site name for file naming
        x_label (str): X-axis label for plot
        y_label (str): Y-axis label for plot
        plot_title (str): Plot title
    """
    start_time = process_time()
    
    # Export to Excel
    ap.AddMessage("Exporting data to Excel")
    excel_file = os.path.join(output_folder, f"{site_name}_elevation_profile_data.xlsx")
    ap.conversion.TableToExcel(elevation_points, excel_file, "ALIAS")
    
    # Extract data for plotting
    ap.AddMessage("Preparing data for plotting")
    x_data, y_data = [], []
    with ap.da.SearchCursor(elevation_points, ["distance_m", "elevation_m"]) as cursor:
        for row in cursor:
            if row[1] is not None:  # Skip null elevation values
                x_data.append(row[0])
                y_data.append(row[1])
    
    # Create plot
    ap.AddMessage("Creating elevation profile plot")
    plt.figure(figsize=(12, 6))
    plt.plot(x_data, y_data, 'b-', linewidth=2, label=site_name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_title)
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Save plot
    plot_file = os.path.join(output_folder, f"{site_name}_elevation_profile.png")
    plt.savefig(plot_file, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    elapsed_time = process_time() - start_time
    ap.AddMessage(f"Data export and plotting completed in {elapsed_time:.2f} seconds")
    ap.AddMessage(f"Excel file saved: {excel_file}")
    ap.AddMessage(f"Plot saved: {plot_file}")

def main():
    """Main execution function."""
    try:
        # Get input parameters
        root_path = ap.GetParameterAsText(0)        # Folder
        input_line = ap.GetParameterAsText(1)       # Feature Class
        line_length_field = ap.GetParameterAsText(2)  # Field
        site_name = ap.GetParameterAsText(3)        # String
        wkt = ap.GetParameterAsText(4)              # Spatial Reference
        point_distance = ap.GetParameterAsText(5)   # Linear Unit
        input_raster = ap.GetParameterAsText(6)     # Raster Layer
        x_label = ap.GetParameterAsText(7)          # String
        y_label = ap.GetParameterAsText(8)          # String
        plot_title = ap.GetParameterAsText(9)       # String
        
        # Start processing
        start_time = datetime.now()
        ap.AddMessage(f"Started processing at: {start_time.strftime('%H:%M:%S')}")
        process_start = process_time()
        
        # Validate coordinate system
        coord_sys = validate_coordinate_system(wkt)
        
        # Create processing environment
        temp_gdb, output_folder = create_processing_environment(root_path, site_name)
        
        # Validate and process input line
        processed_line, line_length = validate_and_reproject_line(
            input_line, line_length_field, coord_sys, temp_gdb, site_name
        )
        
        # Generate elevation points
        elevation_points = generate_elevation_points(
            processed_line, point_distance, input_raster, temp_gdb
        )
        
        # Calculate distances
        calculate_distances(elevation_points, point_distance, line_length)
        
        # Export data and create plots
        export_and_plot_data(elevation_points, output_folder, site_name, 
                            x_label, y_label, plot_title)
        
        # Final timing
        end_time = datetime.now()
        total_time = process_time() - process_start
        ap.AddMessage(f"Processing completed at: {end_time.strftime('%H:%M:%S')}")
        ap.AddMessage(f"Total processing time: {timedelta(seconds=total_time)}")
        ap.AddMessage(f"Output folder: {output_folder}")
        
    except ap.ExecuteError:
        msgs = ap.GetMessages(2)
        ap.AddError(msgs)
        print(msgs)
        
    except Exception as e:
        tb = sys.exc_info()[2]
        tbinfo = traceback.format_tb(tb)[0]
        pymsg = f"PYTHON ERRORS:\nTraceback info:\n{tbinfo}\nError Info:\n{str(e)}"
        ap.AddError(pymsg)
        print(pymsg)

if __name__ == "__main__":
    main()
