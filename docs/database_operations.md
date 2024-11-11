# Database Operations

## How to Populate Local Database

### Steps to Populate Your Local Database

1. **Pull Latest Changes**:
   - Ensure you have the latest version of the project files, including `sample_data.json`, from the repository:
     - `git pull origin main`

2. **Apply Migrations**:
   - Apply any new migrations to update the database schema:
     - `python manage.py migrate`

3. **Load Data from JSON**:
   - Load the sample data into your local database:
     - `python manage.py loaddata sample_data.json`

## How to Save Database to Remote Repository

### Steps to Save Your Database to the Remote Repository

1. **Dump Data to JSON**:
   - Export the current state of your database to a JSON file named `sample_data.json`:
     - `python manage.py dumpdata > sample_data.json`

2. **Commit JSON File**:
   - Add the JSON file to your version control system, commit the changes, and push to the remote repository:
     - `git add sample_data.json`
     - `git commit -m "Update database dump"`
     - `git push origin main`

# Remove the existing database
rm db.sqlite3

# Remove existing migration files
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Create new migrations and apply them
python manage.py makemigrations
python manage.py migrate

# Load data from a JSON file (optional)
python manage.py loaddata path/to/your/file.json
