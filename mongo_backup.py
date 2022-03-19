import pymongo
import yaml
import pandas as pd
import os
import sys
from pathlib import Path

main_client = pymongo.MongoClient(
    "mongodb://user:pwd@34.209.114.102/CUSTOM_PIPELINES_CONFIGS")

main_db = main_client['CUSTOM_PIPELINES_CONFIGS']

main_col = main_db['SCADA_PIPELINE_CONFIGS']

cursor_to_configs = main_col.find({})

ss={}

df= pd.DataFrame()

# DIRECTORY DETAILS
parent_dir = Path(__file__).resolve().parent
os.chdir(parent_dir)
sys.path.insert(0, parent_dir)

# DIRECTORY RELATED VARIABLES
output_path = parent_dir /'config_store'
output_path.mkdir(exist_ok=True, parents=True)

def main():
    count = 0
    os.chdir(output_path)
    for config in cursor_to_configs:
        del config['_id']
        file_name= config.get('config_name')
        with open(file_name,'w') as file:
            yaml.dump(config,file)
            file.close()
        # print(config)
        count=count+1
    cursor_to_configs.close()
    print(f'stored {count} configuration files')


if __name__ == '__main__':
    main()
