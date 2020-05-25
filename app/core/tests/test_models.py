from django.test import TestCase
from django.contrib.auth import get_user_model


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

    def test_test_new_user_email_normalized(self):
        """Test that email for new user is normalized."""
        email = "abc@ge.com"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating  user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_new_superuser(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser(
            'testabc@ge.com',
            'mypass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
