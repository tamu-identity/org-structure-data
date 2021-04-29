import json
import csv
import os

# Loop through all the CSV files in the folder
for filename in os.listdir('csv'):
  
  # Create empty dictionary data structure
  LIST = {}

  # Get the name of the set from the CSV filename
  file_name = os.path.basename(filename)

  # Store the file name without the extension
  split_string = file_name.split(".", 1) 
  set_name = split_string[0]

  # Open relevant CSV file
  with open(f'csv/{filename}') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    # Iterate over rows in CSV file
    for row in csv_reader:
      code = row['code']
      if code in LIST:
        # If we've seen this code before, add new item to the 'units' dictionary
        LIST[code]['units'][row['unit_code']] = row['unit_name']
      else:
        # If we haven't, then add a new object to the main dictionary
        parent_object = {
          'name': row['name'],
          'code': row['code'],
          'units': {
            row['unit_code']: row['unit_name']
          }
        }
        LIST[code] = parent_object

  # Write the JSON out to a file, using set_name
  with open(f'json/{set_name}.json', 'w', encoding='utf-8') as fp:
    json.dump(LIST, fp, ensure_ascii=False, indent=4)