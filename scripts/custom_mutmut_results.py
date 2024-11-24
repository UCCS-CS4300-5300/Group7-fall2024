# custom_mutmut_results.py
import json
import os

def load_results():
    # Load the mutmut-stats.json file
    stats_file_path = os.path.join(os.getcwd(), 'mutants', 'mutmut-stats.json')
    with open(stats_file_path, 'r') as f:
        stats = json.load(f)
    return stats

def print_results(stats):
    # Example: Print the basic structure and a few key details
    print("Mutation Testing Results")
    print("="*30)
    print(f"Total tests run: {len(stats['tests_by_mangled_function_name'])}")
    print(f"Duration by test (sample): {list(stats['duration_by_test'].items())[:5]}")

if __name__ == "__main__":
    try:
        stats = load_results()
        print_results(stats)
    except Exception as e:
        print(f"Error: {e}")
