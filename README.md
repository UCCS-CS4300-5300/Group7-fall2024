# Optimal Performance Platform

## Project Overview
This project allows users to select and build computer parts from a database, ensuring compatibility and optimal performance. It leverages Django and Django REST Framework to provide a robust API and web interface.


## Requirements
- Python 3.12
- Django 4.2.11
- Django REST Framework 3.15.2
- PostgreSQL (or another database system)
- Virtual environment tool (like `venv`)


## Authors


## Setting Up the Optimal_Performance_Platform Project

### Steps to Create a Fresh Project
#### 1. Clone the Repository:
- git clone https://github.com/UCCS-CS4300-5300/Group7-fall2024.git
- cd Group7-fall2024

#### 2. Set Up Virtual Environment:
- python -m venv optimalvenv

#### 3. Activate Virtual Environment:
- source optimalvenv/bin/activate

#### 4. Install Dependencies:
- pip install -r requirements.txt

#### 5. Refresh Git’s Index to Apply .gitignore(THIS IS IMPORTANT):

##### a.  Remove all cached entries:
- git rm -r --cached .

##### b.  Re-add files:
- git add .

##### c.  Commit changes:
- git commit -m "Refresh Git index to apply .gitignore"

#### 6. Apply Migrations:
- python manage.py makemigrations
- python manage.py migrate

#### 7. Collect Static Files:
- python manage.py collectstatic

#### 8.  Load Sample Data:
- ##### Ensure `sample_data.json` is in the same directory as `manage.py`:
    - python manage.py loaddata sample_data.json

#### 9. Run the Development Server:
- python manage.py runserver

#### 10. Access the Admin Site
- ##### Create a superuser if you haven’t already:
    - python manage.py createsuperuser
- ##### Log in to the admin site by hitting the "App" button on the devedu page:
    - Add the admin url onto the end of the URL. ex. "http://...devedu.io/admin/"


## Project Structure
- Group7-fall2024: Root project directory.
- Optimal_Performance_Platform/: Main project directory. The main project contains settings and high level urls.
- home/: The main app containing models, views, serializers, and templates.
- home/models.py: Defines the database models.
- home/views.py: Handles API endpoints and views.
- home/serializers.py: Serializes model data.
- home/urls.py: lower level URLs specific the 'home' app.
- home/templates/: Contains HTML templates.
- home/tests.py: Contains unit tests.
- home/static/: Contains static(local) files gathered by the collectstatic command.
- requirements.txt: Lists all dependencies.
- sample_data.json: This is a .json String that contains all of the data contained in our database. 


## Key Commands
- Create Migrations - python manage.py makemigrations
- Apply Migrations - python manage.py migrate
- Collect Static Files - python manage.py collectstatic
- Run Server - python manage.py runserver
- Run Tests - python manage.py test


## Testing

### 1. Run Tests
python manage.py test

## Key Commands
- Create Migrations: python manage.py makemigrations
- Apply Migrations: python manage.py migrate
- Collect Static Files: python manage.py collectstatic
- Run Server: python manage.py runserver
- Run Tests: python manage.py test