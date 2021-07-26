#!/usr/bin/env python3

# ---------------------------------------------------------------- #
# Author: Jonathan Licari
# File: 
# Compares data columns from xlsx files and outputs the
# the items that have been updated into a new spreadsheet 
# ---------------------------------------------------------------- #

import pandas as pd
from pathlib import Path

# Path assignment  
source_folder = Path("Z:/WWD_Serv/Team/JonathanL/CIA/")
output_folder = Path("Z:/WWD_Serv/Team/JonathanL/CIA/output")
output_file_name = "output/Updated RD List.xlsx"

# Baseline Column Headers  
baseline_ID_title = "ID"
baseline_value_title = "Last Modified On"

# Current Revision Column Headers  
current_ID_title = "ID"
current_value_title = "Last Modified On"

# ---------------------------------------------------------------- #
# Function: match_keys                                             #
# ---------------------------------------------------------------- #
# Inputs: hash1, hash2
# Output: updated_ID
# Description:                                                     #
# ---------------------------------------------------------------- #
# iterate through hash1                                            #
#   for each key, search h2 for a matching key                     #
#       if a matching key exists, compare the values               #
#           if values do not match, store the key value in a list  #
#       if key has no match, store the key value in a list         #
# ---------------------------------------------------------------- #

def match_keys(hash1, hash2):
    updated_ID = []
    hash1_id = hash1.keys()
    hash2_id = hash2.keys()
    
    for id_index in hash1_id:
        if id_index in hash2_id:
            if (hash1[id_index] != hash2[id_index]):
               updated_ID.append(id_index)   
        else:
            updated_ID.append(id_index) 

    varType = type(updated_ID)
    print(len(updated_ID), "items have been updated in the ", varType)

    return updated_ID

# ---------------------------------------------------------------- #
# Function: fill_excel                                             #
# ---------------------------------------------------------------- #
# Inputs: updated_ID
# Output: none
# Description:                                                     #
# ---------------------------------------------------------------- #
# Output the list of updated items to a spreadhseet                #
# ---------------------------------------------------------------- #

def fill_excel(items):
    # Convert list to output dataframe
    out_df = pd.DataFrame(items)
    out_df.to_excel(output_file_name, index=False)

# -------------------------- #
# Import baseline excel file #
# -------------------------- #

baseline = pd.read_excel(r"RD_14.1_Export.xlsx", sheet_name='Sheet1')
# Remove unwanted data
baseline = baseline.drop(
    ['Object Heading', 'WWD_Derived', 'New CM Tag', 
    'CM Tag', 'EPECS Requirements Data Dictionary'],
 axis=1)

# Create baseline hash map
baseline_hash = {}
basline_keys = baseline[baseline_ID_title].to_list()
baseline_values = baseline[baseline_value_title]
baseline_hash = dict(zip(basline_keys, baseline_values))
#print(baseline_hash['RD60519'])

# --------------------------------- #
# import current version excel file #
# --------------------------------- #

current = pd.read_excel(r"RD_10.21_Export.xlsx", sheet_name= 'Sheet1')
# Remove unwanted data
current = current.drop(
    ['Object Heading', 'WWD_Derived', 'New CM Tag', 
    'CM Tag', 'EPECS Requirements Data Dictionary'],
 axis=1)

# Create current revision hash map 
current_hash = {}
current_keys = current[current_ID_title].to_list()
current_values = current[current_value_title]
current_hash = dict(zip(current_keys, current_values))
#print(current_hash['RD60519'])

# Store updated items in a list
updated_items = []

if (len(baseline_hash) > len(current_hash)):
    updated_items = match_keys(baseline_hash, current_hash)
else:
    updated_items = match_keys(current_hash, baseline_hash)

# Output list to excel spreadsheet
fill_excel(updated_items)



