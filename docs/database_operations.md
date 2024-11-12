###### Document formated with help from Copilot.

# Database Operations

## How to Populate Local Database

### Steps to Populate Your Local Database

1. **Pull Latest Changes**:
   - Ensure you have the latest version of the project files, including `sample_data.json`, from the repository:
     ```bash
     git pull origin main
     ```

2. **Apply Migrations**:
   - Apply any new migrations to update the database schema:
     ```bash
     python manage.py migrate
     ```

3. **Load Data from JSON**:
   - Load the sample data into your local database:
     ```bash
     python manage.py loaddata sample_data.json
     ```

4. **Verify Data**:
   - Open the Django shell to verify the data has been loaded correctly by checking some records in the database:
     ```bash
     python manage.py shell
     ```
   - In the Django shell, run the following commands:
     ```python
     from django.contrib.auth.models import User
     from home.models import Manufacturer, CPU, RAM, Storage, Build

     print(User.objects.all())
     print(Manufacturer.objects.all())
     print(CPU.objects.all())
     print(RAM.objects.all())
     print(Storage.objects.all())
     print(Build.objects.all())
     ```

## How to Save Database to Remote Repository

### Steps to Save Your Database to the Remote Repository

1. **Dump Data to JSON**:
   - Export the current state of your database to a JSON file named `sample_data.json` with proper indentation:
     ```bash
     python manage.py dumpdata --indent 4 > sample_data.json
     ```

2. **Commit JSON File**:
   - Add the JSON file to your version control system, commit the changes, and push to the remote repository:
     ```bash
     git add sample_data.json
     git commit -m "Update database dump"
     git push origin main
     ```

## How to Reset and Re-Populate Local Database

### Steps to Reset and Re-Populate Your Local Database

1. **Remove the Existing Database**:
   - Either run the emptying script:
     ```bash
     python empty_db_script.py
     ```
   - OR manually delete the existing database file:
     ```bash
     rm db.sqlite3
     ```

2. **Remove Existing Migration Files**:
   - Either run the emptying script:
     ```bash
     python empty_db_script.py
     ```
   - OR manually delete all migration files except for the `__init__.py` files:
     ```bash
     find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
     find . -path "*/migrations/*.pyc" -delete
     ```

3. **Create New Migrations and Apply Them**:
   - Create new migration files and apply them to set up the database schema:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

4. **Load Data from a JSON File (Optional)**:
   - Optionally, load data from the JSON file to populate the database:
     ```bash
     python manage.py loaddata sample_data.json
     ```

5. **Verify Data**:
   - Open the Django shell to verify the data has been loaded correctly by checking some records in the database:
     ```bash
     python manage.py shell
     ```
   - In the Django shell, run the following commands:
     ```python
     from django.contrib.auth.models import User
     from home.models import Manufacturer, CPU, RAM, Storage, Build

     print(User.objects.all())
     print(Manufacturer.objects.all())
     print(CPU.objects.all())
     print(RAM.objects.all())
     print(Storage.objects.all())
     print(Build.objects.all())
     ```

6. **Check Migration Status** (Optional but Useful):
   - Check which migrations have been applied and which are pending:
     ```bash
     python manage.py showmigrations
     ```
