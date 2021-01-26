from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve
from .forms import CustomUserCreationForm
from .views import SignupPageView

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


class SignUpPageTest(TestCase):
    
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'signup.html')
        self.assertContains(self.response,'Sign Up')
        self.assertNotContains(self.response,'Hello World!')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,CustomUserCreationForm)
        self.assertContains(self.response,'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__,SignupPageView.as_view().__name__)

