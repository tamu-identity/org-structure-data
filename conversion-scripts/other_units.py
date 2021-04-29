# Import necessary standard libraries
import json
import csv

# Create empty dictionary data structure
OTHER = {}

# Open relevant CSV file
with open('../csv/other_units.csv') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  # Iterate over rows in CSV file
  for row in csv_reader:
    other_code = row['other_code']
    if other_code in OTHER:
      # If we've seen this Other Code before, add new item to the 'units' dictionary
      OTHER[other_code]['units'][row['unit_code']] = row['unit_name']
    else:
      # If we haven't, then add a new Other object to the main dictionary
      other_object = {
        'name': row['other_name'],
        'code': row['other_code'],
        'units': {
          row['unit_code']: row['unit_name']
        }
      }
      OTHER[other_code] = other_object 

# Now we write the final data structure out to JSON
with open('../json/other_units.json', 'w', encoding='utf-8') as f:
    json.dump(OTHER, f, ensure_ascii=False, indent=4)