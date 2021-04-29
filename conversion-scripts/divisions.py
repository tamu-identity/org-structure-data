# Import necessary standard libraries
import json
import csv

# Create empty dictionary data structure
DIVISIONS = {}

# Open relevant CSV file
with open('../csv/divisions.csv') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  # Iterate over rows in CSV file
  for row in csv_reader:
    division_code = row['division_code']
    if division_code in DIVISIONS:
      # If we've seen this Division Code before, add new item to the 'units' dictionary
      DIVISIONS[division_code]['units'][row['unit_code']] = row['unit_name']
    else:
      # If we haven't, then add a new Division object to the main dictionary
      division_object = {
        'name': row['division_name'],
        'code': row['division_code'],
        'units': {
          row['unit_code']: row['unit_name']
        }
      }
      DIVISIONS[division_code] = division_object 

# Now we write the final data structure out to JSON
with open('../json/divisions.json', 'w', encoding='utf-8') as f:
    json.dump(DIVISIONS, f, ensure_ascii=False, indent=4)