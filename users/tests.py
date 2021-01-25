from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):

    def test_create_user(self):

        User = get_user_model()
        user = User.objects.create_user(username="zico",email="zico@frankchuka.com",password="testing123")

        self.assertEqual(user.username,'zico')
        self.assertEqual(user.email,'zico@frankchuka.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):

        User = get_user_model()
        user = User.objects.create_superuser(username='ukemel',email='ukemel@frankchuka.com',password='testing123')

        self.assertEqual(user.username,'ukemel')
        self.assertEqual(user.email,'ukemel@frankchuka.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)