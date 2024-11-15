# debug_mutmut_results.py
import json
import os

# Load the mutmut-stats.json file
stats_file_path = os.path.join(os.getcwd(), 'mutants', 'mutmut-stats.json')
with open(stats_file_path, 'r') as f:
    stats = json.load(f)

# Print the contents of the file
print(json.dumps(stats, indent=2))
