import pandas as pd
import yaml
from collections import defaultdict
import glob

def extract_keys_from_yaml(file_path, extracted_data):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    for entry in data:
        extracted_data['Namespace'].append('vmm')
        extracted_data['Error Code'].append('VMM-'+str(entry['code']))
        extracted_data['Error Group'].append(entry['errorGroup'])
        extracted_data['Status Code'].append('')
        extracted_data['Severity'].append(entry['severity'])
        extracted_data['Message'].append(entry['message'])
        extracted_data['Action'].append('')

yaml_files = glob.glob('*.yaml')
yaml_files.sort()
extracted_data = defaultdict(list)
for file_name in yaml_files:
    print("Processing file: ", file_name)
    extract_keys_from_yaml(file_name, extracted_data)
    print("rows extracted: ", len(extracted_data['Error Code']))
df = pd.DataFrame.from_dict(extracted_data)
df.to_csv('output.csv', index=False)
