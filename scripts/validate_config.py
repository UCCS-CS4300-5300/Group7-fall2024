# validate_config.py
import configparser
import os

def load_config(file_path):
    config_parser = configparser.ConfigParser()
    if os.path.exists(file_path):
        config_parser.read(file_path)
        return dict(config_parser['mutmut'])
    return None

# Load configuration
setup_cfg_config = load_config('setup.cfg')
print("`setup.cfg` Config:", setup_cfg_config)
