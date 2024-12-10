# scripts/run_all_scripts.py
import os
import sys
import subprocess

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_script(script_path):
    """Function to run a script using subprocess"""
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{script_path} ran successfully.\n")
        print(result.stdout)
    else:
        print(f"Error running {script_path}:\n{result.stderr}")

# Define the list of scripts to run in order
scripts = [
    'empty_db.py',  # Ensure the database is cleared before starting
    'create_manufacturers.py',  # Must run before creating motherboards
    'create_attributes.py',  # Must be done before setting up components
    'create_storages.py',  # Setup storage before builds
    'create_ram.py',  # Setup RAM before builds and motherboards
    'create_motherboards.py',  # Setup motherboards after manufacturers and attributes
    'create_cpus.py',  # Setup CPUs after attributes
    'create_users_profiles.py',  # Create user profiles
    'create_builds.py'  # Create builds after everything else
]

# Run each script
for script in scripts:
    script_path = os.path.join(os.path.dirname(__file__), script)
    run_script(script_path)
