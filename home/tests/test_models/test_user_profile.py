import os
import django
from django.test import TestCase
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from home.models import create_profile, Profile

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Optimal_Performance_Platform.settings')
django.setup()


class UserProfileTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        post_save.disconnect(create_profile, sender=User)

    @classmethod
    def tearDownClass(cls):
        post_save.connect(create_profile, sender=User)
        super().tearDownClass()

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        try:
            self.profile = Profile.objects.get(user=self.user)
        except Profile.DoesNotExist:
            self.profile = Profile.objects.create(user=self.user, profile_name='Test Profile')

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.profile_name, 'Test Profile')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('password'))

    def test_profile_signal(self):
        post_save.connect(create_profile, sender=User)
        new_user = User.objects.create_user(username='newuser', password='password')
        self.assertTrue(Profile.objects.filter(user=new_user).exists())
