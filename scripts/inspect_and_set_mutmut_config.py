# inspect_and_set_mutmut_config.py
import configparser
import os
import subprocess

def load_config(file_path):
    config_parser = configparser.ConfigParser()
    if os.path.exists(file_path):
        config_parser.read(file_path)
        return config_parser['mutmut']
    return None

# Load the .mutmut.ini file first, fallback to setup.cfg if needed
mutmut_ini_config = load_config('.mutmut.ini')
setup_cfg_config = load_config('setup.cfg')

if mutmut_ini_config:
    paths_to_mutate = mutmut_ini_config.get('paths_to_mutate', 'home/')
    backup = mutmut_ini_config.get('backup', 'false') == 'true'
elif setup_cfg_config:
    paths_to_mutate = setup_cfg_config.get('paths_to_mutate', 'home/')
    backup = setup_cfg_config.get('backup', 'false') == 'true'
else:
    paths_to_mutate = 'home/'
    backup = False

# Create .mutmut.ini file if not exists
config_path = '.mutmut.ini'
if not os.path.exists(config_path):
    with open(config_path, 'w') as f:
        f.write('[mutmut]\n')
        f.write(f'paths_to_mutate = {paths_to_mutate}\n')
        f.write(f'backup = {str(backup).lower()}\n')

# Run mutmut with the current configuration
subprocess.run(["mutmut", "run"])
subprocess.run(["mutmut", "results"])
