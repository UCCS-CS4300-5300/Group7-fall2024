# enhanced_mutmut_results.py
import json
import os

def load_results():
    stats_file_path = os.path.join(os.getcwd(), 'mutants', 'mutmut-stats.json')
    with open(stats_file_path, 'r') as f:
        stats = json.load(f)
    return stats

def print_results(stats):
    print("Mutation Testing Results")
    print("="*30)
    print(f"Total tests run: {len(stats['tests_by_mangled_function_name'])}\n")
    
    print("Sample of Test Durations:")
    for test, duration in list(stats['duration_by_test'].items())[:5]:
        print(f"  {test}: {duration:.5f} seconds")
    
    print("\nDetails for Surviving Mutations:")
    for test_name, related_tests in stats['tests_by_mangled_function_name'].items():
        if not related_tests:
            print(f"  {test_name} - Survived")

if __name__ == "__main__":
    try:
        stats = load_results()
        print_results(stats)
    except Exception as e:
        print(f"Error: {e}")
