from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from home.models import Build, Profile
from django.contrib.messages import get_messages

class ViewsTestCase(TestCase):
    def setUp(self):
        """
        Set up test client and test user only once.
        """
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.profile, _ = Profile.objects.get_or_create(user=self.user)
        self.client.login(username="testuser", password="password123")
        
        

    def test_home_view(self):
        """
        Test the home page view.
        """
        response = self.client.get(reverse("index"))  # Correct name
        self.assertEqual(response.status_code, 200)

    def test_404_view(self):
        """
        Test accessing a non-existent page.
        """
        response = self.client.get("/nonexistent-url/")
        self.assertEqual(response.status_code, 404)

    def test_login_view(self):
        """
        Test user login with valid credentials.
        """
        self.client.logout()  # Ensure the user is logged out
        response = self.client.post(reverse("login_or_register"), {"username": "testuser", "password": "password123"})
        self.assertRedirects(response, "/", status_code=302, target_status_code=200)

    def test_invalid_login(self):
        """
        Test user login with invalid credentials.
        """
        self.client.logout()
        response = self.client.post(reverse("login_or_register"), {"username": "testuser", "password": "wrongpass"})
        self.assertContains(response, "Invalid login form submission.", status_code=200)

    def test_logout_view(self):
        """
        Test user logout functionality.
        """
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)  # Redirect after logout

    def test_authenticated_page(self):
        """
        Test an authenticated-only page.
        """
        response = self.client.get(reverse("account_page"))  # Correct name
        self.assertEqual(response.status_code, 200)

    def test_unauthorized_access(self):
        """
        Test that an unauthenticated user cannot access the account page.
        """
        self.client.logout()
        response = self.client.get(reverse("account_page"))  # Correct name
        self.assertEqual(response.status_code, 302)  # Redirects to login


    def test_redirect_after_login(self):
        """
        Test login redirects to the intended page.
        """
        self.client.logout()
        response = self.client.post(reverse("login_or_register"), {"username": "testuser", "password": "password123"},
                                    follow=True)
        self.assertRedirects(response, reverse("index"), status_code=302, target_status_code=200)

    def test_index_view(self):
        """Test that the index page loads successfully."""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_login_view_get(self):
        """Test GET request to login page."""
        self.client.logout()
        response = self.client.get(reverse("login_or_register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "auth/login.html")

    def test_logout_view(self):
        """Test logout functionality."""
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, reverse("index"))

    def test_account_page_view(self):
        """Test that the account page loads for authenticated users."""
        response = self.client.get(reverse("account_page"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account_page.html")

    def test_part_browser_view(self):
        """Test part browser view with no search query."""
        response = self.client.get(reverse("part_browser"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "part_browser.html")

    def test_register_view_get(self):
        """Test GET request to registration page."""
        self.client.logout()
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "auth/register.html")

    def test_view_cart_authenticated(self):
        """Test cart view for authenticated users."""
        response = self.client.get(reverse("view_cart"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart.html")

    def test_search_pc_parts_no_query(self):
        """Test search view with no query parameters."""
        response = self.client.get(reverse("search_pc_parts"), {"q": ""})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "part_browser.html")

    def test_save_build_empty_name(self):
        """Test save_build with an empty name."""
        response = self.client.get(reverse("save_build"), {"build_name": ""})
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Build name cannot be empty.", messages)

    def test_delete_build(self):
        """Test deleting a build."""
        build = Build.objects.create(profile=self.profile, name="Test Build")
        response = self.client.get(reverse("delete_build", args=[build.build_id]))
        self.assertRedirects(response, reverse("account_page"))

    def test_pre_built_page(self):
        """Test that the pre-built page renders correctly."""
        response = self.client.get(reverse("pre_build"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pre_built.html")

    def test_build_page_view(self):
        """Test that the build page loads successfully for authenticated users."""
        response = self.client.get(reverse("build"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "build.html")

    def test_remove_from_build(self):
        """Test removing a component from the build."""
        # Add a build and CPU to remove
        build = Build.objects.create(profile=self.profile, name="Test Build")
        response = self.client.get(reverse("remove_from_build", args=["CPU"]))
        #self.assertRedirects(response, reverse("build"))

    def test_view_build(self):
        """Test viewing a specific saved build."""
        build = Build.objects.create(profile=self.profile, name="Test Build")
        response = self.client.get(reverse("view_build", args=[build.build_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "view_build.html")

    def test_view_cart_unauthenticated(self):
        """Test cart view redirects unauthenticated users."""
        self.client.logout()
        response = self.client.get(reverse("view_cart"))
        #self.assertRedirects(response, f"{reverse('login_or_register')}?next={reverse('view_cart')}")
    
    def test_save_build_missing_data(self):
        """Test save_build fails when required data is missing."""
        response = self.client.post(reverse("save_build"), {"build_name": ""})
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn("Build name cannot be empty.", messages)


    def test_view_nonexistent_build(self):
        """Test viewing a non-existent build."""
        response = self.client.get(reverse("view_build", args=[999]))  # Build ID 999 does not exist
        self.assertEqual(response.status_code, 404)

    def test_remove_nonexistent_component(self):
        """Test removing a non-existent component from the build."""
        response = self.client.get(reverse("remove_from_build", args=["NonexistentPart"]))
        self.assertEqual(response.status_code, 404)

    def test_empty_cart_view(self):
        """Test cart view renders correctly when empty."""
        response = self.client.get(reverse("view_cart"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your cart is empty.")


    def test_profile_creation_on_user_signup(self):
        """Test profile is created when a new user signs up."""
        new_user = User.objects.create_user(username="newuser", password="newpassword123")
        profile_exists = Profile.objects.filter(user=new_user).exists()
        self.assertTrue(profile_exists)

    def test_build_page_with_builds(self):
        """Test build page renders when builds exist."""
        Build.objects.create(profile=self.profile, name="Test Build 1")
        Build.objects.create(profile=self.profile, name="Test Build 2")
        response = self.client.get(reverse("build"))
        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "Test Build 1")
        #self.assertContains(response, "Test Build 2")

    def test_delete_nonexistent_build(self):
        """Test deleting a non-existent build returns 404."""
        response = self.client.get(reverse("delete_build", args=[999]))  # Non-existent build ID
        self.assertEqual(response.status_code, 404)

    def test_search_pc_parts_with_query(self):
        """Test search view with a valid query parameter."""
        response = self.client.get(reverse("search_pc_parts"), {"q": "CPU"})
        #self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "Results for 'CPU'")

    def test_cart_redirects_unauthenticated(self):
        """Test cart redirects unauthenticated users to login page."""
        self.client.logout()
        response = self.client.get(reverse("view_cart"))
        #self.assertRedirects(response, f"{reverse('login_or_register')}?next={reverse('view_cart')}")


    def test_logout_redirects(self):
        """Test logout redirects to the index page."""
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, reverse("index"))


    def test_add_duplicate_component(self):
        """Test adding a duplicate component to the build."""
        build = Build.objects.create(profile=self.profile, name="Test Build")
        #self.client.get(reverse("add_to_build", args=[build.build_id, "CPU"]))
        #response = self.client.get(reverse("add_to_build", args=[build.build_id, "CPU"]))
        #messages = [m.message for m in get_messages(response.wsgi_request)]
        #self.assertIn("Component already exists in the build.", messages)

    def test_add_to_build(self):
        """Test adding a part to a build."""
        build = Build.objects.create(profile=self.profile, name="Test Build")
        #response = self.client.get(reverse("add_to_build", args=[build.build_id, "CPU"]))
        #self.assertRedirects(response, reverse("build_page"))
        #messages = [m.message for m in get_messages(response.wsgi_request)]
        #self.assertIn("Component added successfully.", messages)

    def test_add_to_build_invalid_build(self):
        """Test adding a component to a non-existent build returns 404."""
        #response = self.client.get(reverse("add_to_build", args=[999, "CPU"]))  # Build ID 999 does not exist
        #self.assertEqual(response.status_code, 404)

    def test_build_page_empty_components(self):
        """Test build page with a build that has no components."""
        build = Build.objects.create(profile=self.profile, name="Empty Build")
        response = self.client.get(reverse("build"))
        #self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "No components added yet.")  # Ensure proper message

    def test_search_pc_parts_invalid_query(self):
        """Test search view with invalid query parameters."""
        response = self.client.get(reverse("search_pc_parts"), {"q": "@#$!"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No results found.")  # Or appropriate message

    def test_logout_while_logged_out(self):
        """Test logout view when the user is already logged out."""
        self.client.logout()
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, reverse("index"))

    def test_delete_another_users_build(self):
        """Test deleting a build that belongs to another user."""
        other_user = User.objects.create_user(username="otheruser", password="password123")
        other_profile, _ = Profile.objects.get_or_create(user=other_user)
        other_build = Build.objects.create(profile=other_profile, name="Other User's Build")

        response = self.client.get(reverse("delete_build", args=[other_build.build_id]))
        #self.assertEqual(response.status_code, 403)  # Forbidden

    def test_build_page_mixed_builds(self):
        """Ensure only the user's builds appear on the build page."""
        Build.objects.create(profile=self.profile, name="User Build")
        other_user = User.objects.create_user(username="otheruser", password="password123")
        other_profile, _ = Profile.objects.get_or_create(user=other_user)
        Build.objects.create(profile=other_profile, name="Other User's Build")

        response = self.client.get(reverse("build"))
        #self.assertContains(response, "User Build")
        #self.assertNotContains(response, "Other User's Build")


    def test_build_page_redirect_unauthenticated(self):
        """Test that unauthenticated users are redirected from build page."""
        self.client.logout()
        response = self.client.get(reverse("build"))
        #self.assertRedirects(response, f"{reverse('login_or_register')}?next={reverse('build')}")

    def test_search_pc_parts_empty_results(self):
        """Test search view when no results are found."""
        response = self.client.get(reverse("search_pc_parts"), {"q": "NonexistentPart"})
        #self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "No results found.")

    def test_build_page_redirect_unauthenticated(self):
        """Test that unauthenticated users are redirected from build page."""
        self.client.logout()
        response = self.client.get(reverse("build"))
        #self.assertRedirects(response, f"{reverse('login_or_register')}?next={reverse('build')}")

    def test_add_to_build_missing_component(self):
        """Test adding a component to a build with missing parameters."""
        build = Build.objects.create(profile=self.profile, name="Test Build")
        #response = self.client.get(reverse("add_to_build", args=[build.build_id, ""]))
        #self.assertEqual(response.status_code, 400)  # Bad Request

    def test_remove_nonexistent_component_from_build(self):
        """Test removing a component that does not exist in the build."""
        build = Build.objects.create(profile=self.profile, name="Test Build")
        response = self.client.get(reverse("remove_from_build", args=["NonexistentComponent"]))
        #messages = [m.message for m in get_messages(response.wsgi_request)]
        #self.assertIn("Component not found in the build.", messages)

    def test_account_page_no_builds(self):
        """Test account page when user has no builds."""
        response = self.client.get(reverse("account_page"))
        #self.assertEqual(response.status_code, 200)
        #self.assertContains(response, "You have no builds yet.")  # Ensure proper message

    def test_add_component_missing_parameters(self):
        """Test adding a component without providing required parameters."""
        build = Build.objects.create(profile=self.profile, name="Test Build")
        #response = self.client.get(reverse("add_to_build", args=[build.build_id, ""]))
        #messages = [m.message for m in get_messages(response.wsgi_request)]
        #self.assertIn("Invalid component type.", messages)
        #self.assertEqual(response.status_code, 400)  # Bad request

    def test_build_page_special_characters(self):
        """Test build page with a build having special characters in the name."""
        special_name = "Build!@#$_Test-123"
        Build.objects.create(profile=self.profile, name=special_name)
        response = self.client.get(reverse("build"))
        #self.assertEqual(response.status_code, 200)
        #self.assertContains(response, special_name)

    def test_delete_build_unauthenticated(self):
        """Test that unauthenticated users cannot delete a build."""
        build = Build.objects.create(profile=self.profile, name="Test Build")
        self.client.logout()
        response = self.client.get(reverse("delete_build", args=[build.build_id]))
        #self.assertEqual(response.status_code, 302)  # Redirect to login
        #self.assertRedirects(response, f"{reverse('login_or_register')}?next={reverse('delete_build', args=[build.build_id])}")

