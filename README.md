# Optimal Performance Platform

### **For:** CS4300 at UCCS
### **When:** Fall 2024
### **By:** Daniel Buck | Joel Flinn | Jagger Z | Neako Hallisey | Jesse Merideth
### CS4300 by Dr. Hastings
### Fall 2024 at UCCS

## Notice on AI
#### NOTE: AI was used for tasks such as formatting text, searching for documentation, error resolution, comment skeletons, etc.


## Project Overview
### This project allows users to select and build computer parts from a database, ensuring compatibility and optimal performance. It leverages Django and Django REST Framework to provide a robust API and web interface.

## Requirements
- Python 3.12
- Django 4.2.11
- Django REST Framework 3.15.2
- PostgreSQL (or another database system)
- Virtual environment tool (like `venv`)


## License Information
### NOTE: At this time we have not finalized our decision on what license to use. Below are our considerations.
#### MIT License
Pros:
- Permissive: Allows for almost unrestricted use, modification, and distribution.
- Simple: Short and easy to understand.
- Wide Adoption: Popular in the open-source community, promoting collaboration.

Cons:
- Less Protection: Offers minimal protection for contributors regarding liability and warranty.
- Patent Risks: Doesn’t explicitly address patent rights.

Examples:
- Use: Small utilities, open-source projects aimed at broad adoption, educational projects.
- Avoid: Projects requiring strong copyleft principles or patent protections.

#### Apache 2.0 License
Pros:
- Permissive: Similar to MIT, with extensive freedoms.
- Patent Protection: Includes an explicit grant of patent rights from contributors.
- Comprehensive: Provides more detailed terms, reducing ambiguity.

Cons:
- Lengthy: More complex and longer than the MIT license.
- Contributor Agreement: Requires explicit permission for contributions.

Examples:
- Use: Large-scale projects, projects involving patented technology, or corporate-backed open-source projects.
- Avoid: Projects where simplicity and minimal overhead are prioritized.

#### GNU General Public License (GPL)
Pros:
- Strong Copyleft: Ensures derivative works are also open-source, promoting free software.
- Wide Adoption: Popular for projects aimed at ensuring freedom to use, modify, and distribute.

Cons:
- Restrictive: Requires any derivative work to also be licensed under GPL.
- Compatibility Issues: Can be less compatible with other licenses.

Examples:
- Use: Projects focused on user freedoms, software meant to remain open-source perpetually, collaborative community projects.
- Avoid: Projects where compatibility with other licenses is crucial, or where commercial use and proprietary extensions are expected.


## Setting Up the Optimal_Performance_Platform Project

### Steps to Create a Fresh Project

#### 1. Clone the Repository:
- `git clone https://github.com/UCCS-CS4300-5300/Group7-fall2024.git`
- `cd Group7-fall2024`

#### 2. Set Up Virtual Environment:
- `python -m venv optimalvenv`

#### 3. Activate Virtual Environment:
- `source optimalvenv/bin/activate`

#### 4. Install Dependencies:
- `pip install -r requirements.txt`

#### 5. Apply Migrations:
- python manage.py makemigrations
- python manage.py migrate

#### 6. Collect Static Files:
- python manage.py collectstatic

#### 7.  Load Sample Data:
- ##### Ensure `sample_data.json` is in the same directory as `manage.py`:
    - python manage.py loaddata sample_data.json

#### 8. Run the Development Server:
- python manage.py runserver

### Additional Options

#### Access the Admin Site
- Create a superuser if you haven’t already:
  - `python manage.py createsuperuser`
- Log in to the admin site by hitting the "App" button on the devedu page:
  - Add the admin URL onto the end of the URL. ex. "http://...devedu.io/admin/"

#### Access the API Site
- Log in to the API site by hitting the "App" button on the devedu page:
  - Add the API URL onto the end of the URL. ex. "http://...devedu.io/api/"

## How to Save Data in the Database

### Steps to Dump Data

1. **Dump Data to JSON**:
   - Export your current database to a JSON file:
     - `python manage.py dumpdata > sample_data.json`

2. **Commit JSON File**:
   - Add and commit the JSON file to your repository:
     - `git add sample_data.json`
     - `git commit -m "Update database dump"`
     - `git push origin main`

### Steps to Load Data

1. **Pull Latest Changes**:
   - Ensure you have the latest `sample_data.json` from the repository:
     - `git pull origin main`

2. **Apply Migrations**:
   - Run this step only if there are new migrations:
     - `python manage.py migrate`

3. **Load Data from JSON**:
   - Import the data into your database:
     - `python manage.py loaddata sample_data.json`

### Applying Changes to Models:
- python manage.py makemigrations
- python manage.py migrate


### Refreshing Git’s Index to Apply .gitignore(THIS IS IMPORTANT):

#### a.  Remove all cached entries:
- git rm -r --cached .

#### b.  Re-add files:
- git add .

#### c.  Commit changes:
- git commit -m "Refresh Git index to apply .gitignore"


### Applying Changes to Models:
- python manage.py makemigrations
- python manage.py migrate


### Refreshing Git’s Index to Apply .gitignore(THIS IS IMPORTANT):

#### a.  Remove all cached entries:
- git rm -r --cached .

#### b.  Re-add files:
- git add .

#### c.  Commit changes:
- git commit -m "Refresh Git index to apply .gitignore"


## Project Structure
- Group7-fall2024: Root project directory.
- Optimal_Performance_Platform/: Main project directory. The main project contains settings and high level urls.
- home/: The main app containing models, views, serializers, and templates.
- home/models.py: Defines the database models.
- home/views.py: Handles API endpoints and views.
- home/serializers.py: Serializes model data.
- home/urls.py: Lower level URLs specific to the 'home' app.
- home/templates/: Contains HTML templates.
- home/tests.py: Contains unit tests.
- home/static/: Contains static (local) files gathered by the collectstatic command.
- requirements.txt: Lists all dependencies.
- sample_data.json: This is a .json string that contains all of the data contained in our database.

## Key Commands
- Create Migrations: `python manage.py makemigrations`
- Apply Migrations: `python manage.py migrate`
- Collect Static Files: `python manage.py collectstatic`
- Run Server: `python manage.py runserver`
- Run Tests: `python manage.py test`
- Dump Data: `python manage.py dumpdata > sample_data.json`
- Load Data: `python manage.py loaddata sample_data.json`

## Testing

### 1. Run Tests
- `python manage.py test`
- `coverage run --source='.' manage.py test home.tests`
