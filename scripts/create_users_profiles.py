# scripts/create_users_profiles.py
import os
import sys
import django

# Add the project root to the PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ensure the correct DJANGO_SETTINGS_MODULE path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()

from django.contrib.auth.models import User
from home.models import Profile

# Create Users and Profiles
user, created = User.objects.get_or_create(username='testuser', defaults={'password': 'testpassword'})
profile, created = Profile.objects.get_or_create(user=user, defaults={'profile_name': 'test_profile'})

# Print Results
print('User:', user)
print('Profile:', profile)
