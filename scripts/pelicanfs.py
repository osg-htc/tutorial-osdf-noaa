#!/usr/bin/env python3

"""
Example script for analyzing temperature data for one station, using Pelican FS, OSDF
"""

# ??? import pelicanfs 
import pandas as pd
from my_functions import extract_temp_data, identify_season, create_histogram

# OSDF location of dataset

osdf_prefix = 'osdf:///aws-opendata/us-east-1/noaa-ghcn-pds'

# Get list of stations 

# Original link is `https://noaa-ghcn-pds.s3.amazonaws.com/ghcnd-stations.txt`
station_list_link = f"{osdf_prefix}/ghcnd-stations.txt"
# ??? station_list = pelicanfs.get(station_list_link)

# Identify station
station_search = "WI MADISON"
# ??? possible_stations = [i for i in station_list.readlines() if station_search in i]
#
# for i in possible_stations:
#    print(i)

# Dane Country Regional Airport, Madison, WI, USA
station_name = "WI MADISON DANE CO RGNL AP"
station_id = "USW00014837"  

# Get station data
station_data_link = f"{osdf_prefix}/csv/by_station/{station_id}.csv"
# ??? station_data = pelicanfs.get(station_data_link)


# Read into pandas somehow, then can use... 
station_df = convert_pelicanfs_station_data_to_dataframe()

# Extract Min, Max Temperatures as dataframe
tempdf = extract_temp_data(station_df)

# Describe the dataset
print(f"{tempdf.describe()}\n")

# Label by season
tempdf['SEASON'] = tempdf.index.map(identify_season)

# Create histograms
# Saves as <STATION ID>.png, unless otherwise specified.
create_histogram(tempdf, station_id, f'{station_id}-season-hist.png')
