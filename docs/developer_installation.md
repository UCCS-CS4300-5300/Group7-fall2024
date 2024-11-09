# Developer Installation Instructions

## Setting Up the Optimal Performance Platform Project

### Prerequisites
- Ensure you have Python 3.12 installed.
- Ensure you have PostgreSQL installed and running.

### Steps to Create a Fresh Project

#### 1. Clone the Repository:
- Clone the project repository to your local machine:
  - `git clone https://github.com/UCCS-CS4300-5300/Group7-fall2024.git`
  - `cd Group7-fall2024`

#### 2. Set Up Virtual Environment:
- Create a virtual environment for the project:
  - `python -m venv optimalvenv`

#### 3. Activate Virtual Environment:
- Activate the virtual environment:
  - `source optimalvenv/bin/activate`

#### 4. Install Dependencies:
- Install the project dependencies listed in `requirements.txt`:
  - `pip install -r requirements.txt`

#### 5. Apply Migrations:
- Create and apply database migrations:
  - `python manage.py makemigrations`
  - `python manage.py migrate`

#### 6. Collect Static Files:
- Collect all static files into the static directory:
  - `python manage.py collectstatic`

#### 7. Load Sample Data:
- Ensure `sample_data.json` is in the same directory as `manage.py` and load the sample data into the database:
  - `python manage.py loaddata sample_data.json`

#### 8. Run the Development Server:
- Start the development server:
  - `python manage.py runserver`
