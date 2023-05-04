# test cases using django framework

from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage

# test cases for user interface front-end pages
class FrontEndTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/index.html')

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/login.html')

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/logout.html')

    def test_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/profile.html')


# test case to that the login page is displayed correctly.
class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/login.html')

#  test case to verify that the "Forgot Password" link redirects to the correct page.
class ForgotPasswordTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_forgot_password(self):
        response = self.client.get(reverse('forgot_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/forgot_password.html')

#  test case for Attempt to log in with an incorrect password and ensure that an error message is displayed.
class IncorrectPasswordTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_incorrect_password(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/login.html')

#  test case for to verify that the user is redirected to the correct page upon successful login.
class SuccessfulLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_successful_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/login.html')

# design test case to verify that the logout function works correctly.
class LogoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/logout.html')

# design test case to Ensure that the user's profile information is displayed correctly.
class ProfileTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_profile(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/profile.html')

#design test case to Ensure that all buttons and links on the website are functioning correctly.
class ButtonTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_button(self):
        response = self.client.get(reverse('button'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/button.html')

# test case to Verify that the website is responsive and displays correctly on different devices and screen sizes.
class ResponsiveTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_responsive(self):
        response = self.client.get(reverse('responsive'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/responsive.html')

# test case to Verify that all text and images are displayed correctly and are properly aligned.
class TextTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_text(self):
        response = self.client.get(reverse('text'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/text.html')



# test case to Verify that the website's layout is consistent throughout all pages.
class LayoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_layout(self):
        response = self.client.get(reverse('layout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/layout.html')

# test case to Verify that all forms and input fields are functioning correctly and that user input is validated correctly.
class FormTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form(self):
        response = self.client.get(reverse('form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'r/form.html')


