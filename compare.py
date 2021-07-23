import pandas as pd
from pathlib import Path

# Path assignment  
source_folder = Path("Z:/WWD_Serv/Team/JonathanL/CIA/")
output_folder = Path("Z:/WWD_Serv/Team/JonathanL/CIA/output")

# Baseline Column Headers  
baseline_ID_title = "ID"
baseline_value_title = "Last Modified On"

# Current Revision Column Headers  
current_ID_title = "ID"
current_value_title = "Last Modified On"

# -------------------------- #
# Import baseline excel file #
# -------------------------- #

baseline = pd.read_excel(r"RD_14.1_Export.xlsx", sheet_name='Sheet1')
# Remove unwanted data
baseline = baseline.drop(
    ['Object Heading', 'WWD_Derived', 'New CM Tag', 'CM Tag', 'EPECS Requirements Data Dictionary'],
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
    ['Object Heading', 'WWD_Derived', 'New CM Tag', 'CM Tag', 'EPECS Requirements Data Dictionary'],
 axis=1)

# Create current revision hash map 
current_hash = {}
current_keys = current[current_ID_title].to_list()
current_values = current[current_value_title]
current_hash = dict(zip(current_keys, current_values))
#print(current_hash['RD60519'])

# Export results in spreadsheet
