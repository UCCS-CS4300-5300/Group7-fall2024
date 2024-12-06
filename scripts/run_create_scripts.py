# scripts/run_all_scripts.py
import os
import sys
import subprocess
import django  # Ensure that we import django at the top

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_script(script_path):
    """Function to run a script using subprocess"""
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{script_path} ran successfully.\n")
    else:
        print(f"Error running {script_path}:\n{result.stderr}")

# Ensure the correct DJANGO_SETTINGS_MODULE path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

# Define the list of scripts to run in order
scripts = [
    'scripts/create_users_profiles.py',
    'scripts/create_manufacturers.py',
    'scripts/create_component_attributes.py',
    'scripts/create_components.py',
    'scripts/create_builds.py'
]

# Run each script
for script in scripts:
    run_script(script)
