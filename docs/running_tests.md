# Running Tests

### Prerequisites
- Ensure you have the `coverage` package installed. You can install it using:
  - `pip install coverage`

### Steps to Run Tests

1. **Run Tests**:
   - Run the test suite using Django's test runner:
     - `python manage.py test`

2. **Run Tests with Coverage**:
   - Run the tests and measure code coverage:
     - `coverage run --source='.' manage.py test home/tests`

3. **Generate Coverage Report**:
   - Generate a coverage report to see how much of your code is covered by tests:
     - `coverage report`
