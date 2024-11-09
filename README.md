# Optimal Performance Platform

### **For:** CS4300 at UCCS
### **When:** Fall 2024
### **By:** Daniel Buck | Joel Flinn | Jagger Z | Neako Hallisey | Jesse Meredeth

## Project Overview
This project allows users to select and build computer parts from a database, ensuring compatibility and optimal performance. It leverages Django and Django REST Framework to provide a robust API and web interface.

## Notice on AI
#### NOTE: AI was used for tasks such as formatting text, searching for documentation, error resolution, comment skeletons, etc.

## Documentation
- [Database Schema Documentation](docs/database_schema.md)
- [System Architecture Documentation](docs/system_architecture.md)
- [API Documentation](docs/api_documentation.md)
- [Developer Installation Instructions](docs/developer_installation.md)
- [License Information](docs/license_information.md)
- [Database Operations Guide](docs/database_operations.md)
- [Refresh Git’s Index Guide](docs/refresh_git_index.md)
- [Running Tests Guide](docs/running_tests.md)

## Project Structure
- **Group7-fall2024**: Root project directory.
- **Optimal_Performance_Platform/**: Main project directory. Contains settings and high-level URLs.
- **home/**: The main app containing models, views, serializers, and templates.
  - **home/models.py**: Defines the database models.
  - **home/views.py**: Handles views for the application.
  - **home/views_api.py**: Handles API endpoints.
  - **home/views_render.py**: Handles template rendering views.
  - **home/serializers.py**: Serializes model data.
  - **home/urls.py**: Lower level URLs specific to the 'home' app.
  - **home/templates/**: Contains HTML templates.
  - **home/static/**: Contains static (local) files gathered by the collectstatic command.
  - **home/tests/**: Contains unit tests.
- **requirements.txt**: Lists all dependencies.
- **sample_data.json**: Contains all of the data for the database.

## Key Commands
- **Create Migrations**: `python manage.py makemigrations`
- **Apply Migrations**: `python manage.py migrate`
- **Collect Static Files**: `python manage.py collectstatic`
- **Run Server**: `python manage.py runserver`
- **Run Tests**: `python manage.py test`
- **Dump Data**: `python manage.py dumpdata > sample_data.json`
- **Load Data**: `python manage.py loaddata sample_data.json`
