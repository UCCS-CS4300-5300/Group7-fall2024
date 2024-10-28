# Optimal Performance Platform

## Project Overview
This project allows users to select and build computer parts from a database, ensuring compatibility and optimal performance. It leverages Django and Django REST Framework to provide a robust API and web interface.


## Requirements
- Python 3.12
- Django 4.2.11
- Django REST Framework 3.15.2
- PostgreSQL (or another database system)

## Authors



## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/UCCS-CS4300-5300/Group7-fall2024.git
cd Group7-fall2024

### 2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

WE HAVE NOT NEEDED TO DO THIS YET, BUT IT MAY COME UP AS OUR PROJECT GETS CLOSER TO MVP
### 4. Configure Environment Variables
Create a .env file in the root directory and add your environment variables:

DJANGO_SECRET_KEY='your-secret-key'
DATABASE_NAME='your-database-name'
DATABASE_USER='your-database-user'
DATABASE_PASSWORD='your-database-password'
DATABASE_HOST='your-database-host'
DATABASE_PORT='your-database-port'

### 5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

### 6. Collect Static Files
python manage.py collectstatic

### 7. Run the Development Server
python manage.py runserver


## Testing

### 1. Run Tests
python manage.py test


## Project Structure
- optimal_performance_platform: The main app containing models, views, serializers, and templates.
- optimal_performance_platform/models.py: Defines the database models.
- optimal_performance_platform/views.py: Handles API endpoints and views.
- optimal_performance_platform/serializers.py: Serializes model data.
- optimal_performance_platform/urls.py: URL routing.
- optimal_performance_platform/templates: Contains HTML templates.
- optimal_performance_platform/tests.py: Contains unit tests.

## Key Commands
- Create Migrations: python manage.py makemigrations
- Apply Migrations: python manage.py migrate
- Collect Static Files: python manage.py collectstatic
- Run Server: python manage.py runserver
- Run Tests: python manage.py test