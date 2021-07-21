import pandas as pd
from pathlib import Path

# Import 
source_folder = Path("Z:/WWD_Serv/Team/JonathanL/")
baseline_ID_title = "ID"
baseline_value_title = "Last Modified On"

current_ID_title = "ID"
current_value_title = "Last Modified On"

# import baseline excel file
baseline = pd.read_excel(r"RD_14.1_Export.xlsx", sheet_name='Sheet1')
baseline_keys = pd.DataFrame(baseline, columns = [baseline_ID_title])
baseline_values = pd.DataFrame(baseline, columns = [baseline_value_title])

# import current version excel file
current = pd.read_excel(r"RD_10.21_Export.xlsx", sheet_name= 'Sheet1')
current_keys = pd.DataFrame(current, columns = [current_ID_title])
current_values = pd.DataFrame(current, columns = [current_value_title])

# Check types
print("Current Revision Hash key type: ")
print(type(current_keys))
print("Current Revision Hash value type: ")
print(type(current_values))

print("Baseline Revision Hash key type: ")
print(type(baseline_keys))
print("Current Revision Hash value type: ")
print(type(baseline_values))

print(baseline)
print(baseline_keys)

