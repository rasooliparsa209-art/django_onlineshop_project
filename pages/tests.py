from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class PageTests(TestCase):

    # =========================
    # Status Code Tests
    # =========================

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


    def test_signup_page_status_code(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # =========================
    # Template Tests
    # =========================

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')


    def test_signup_page_template(self):
        response = self.client.get(reverse('signup'))
        self.assertTemplateUsed(response, 'account/signup.html')


    def test_login_page_template(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'account/login.html')


