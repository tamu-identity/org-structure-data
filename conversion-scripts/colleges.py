# Import necessary standard libraries
import json
import csv

# Create empty dictionary data structure
COLLEGES = {}

# Open relevant CSV file
with open('../csv/colleges.csv') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  # Iterate over rows in CSV file
  for row in csv_reader:
    college_code = row['college_code']
    if college_code in COLLEGES:
      # If we've seen this College Code before, add new item to the 'units' dictionary
      COLLEGES[college_code]['units'][row['unit_code']] = row['unit_name']
    else:
      # If we haven't, then add a new College object to the main dictionary
      college_object = {
        'name': row['college_name'],
        'code': row['college_code'],
        'units': {
          row['unit_code']: row['unit_name']
        }
      }
      COLLEGES[college_code] = college_object 

# Now we write the final data structure out to JSON
with open('../json/colleges.json', 'w', encoding='utf-8') as f:
    json.dump(COLLEGES, f, ensure_ascii=False, indent=4)