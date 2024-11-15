# check_mutmut_config.py
import configparser
import os

config = configparser.ConfigParser()

# Load the .mutmut.ini file
config_file_path = os.path.join(os.getcwd(), '.mutmut.ini')
config.read(config_file_path)

# Print the paths_to_mutate value
if 'mutmut' in config:
    paths_to_mutate = config['mutmut'].get('paths_to_mutate', None)
    print("paths_to_mutate:", paths_to_mutate)
else:
    print(".mutmut.ini file not found or incorrectly formatted")

