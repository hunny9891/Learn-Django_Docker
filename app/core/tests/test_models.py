from django.test import TestCase
from django.contrib.auth import  get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_success(self):
        """Test creating a new user with email and password"""
        email = "abc@ge.com"
        password = "P@55word"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))