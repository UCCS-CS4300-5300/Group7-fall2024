# scripts/create_users_profiles.py
import os
import sys
import django

print("Starting create_users_profiles.py script...")

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

print("Django setup completed.")

from django.contrib.auth.models import User
from home.models import Profile

print("Models imported successfully.")

# Create users
users = [
    {
        'username': 'dbuck3',
        'password': 'dbuckpassword',
        'email': 'dbuck3@example.com'
    },
    {
        'username': 'testuser',
        'password': 'testpassword',
        'email': 'testuser@example.com'
    }
]

print("Creating users and profiles...")

for user_data in users:
    user, created = User.objects.get_or_create(username=user_data['username'], defaults={'email': user_data['email']})
    if created:
        user.set_password(user_data['password'])  # Set and hash the password
        user.is_superuser = True  # Set superuser status
        user.is_staff = True  # Set staff status
        user.save()
        print(f"User {user_data['username']} created and password set.")
    else:
        print(f"User {user_data['username']} already exists.")

    # Ensure profile exists for the user
    if not Profile.objects.filter(user=user).exists():
        Profile.objects.create(user=user)
        print(f"Profile for user {user_data['username']} created.")
    else:
        print(f"Profile for user {user_data['username']} already exists.")

print("Completed creating users and profiles.")
