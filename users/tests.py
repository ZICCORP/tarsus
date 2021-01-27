from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse,resolve

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
    username= 'frank'
    email = 'chuka@frankchuka.com'
    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'account/signup.html')
        self.assertContains(self.response,'Sign Up')
        self.assertNotContains(self.response,'Hello World!')

    def test_signup_form(self):
       new_user = get_user_model().objects.create_user(self.username,self.email)
       self.assertEqual(get_user_model().objects.all().count(),1)
       self.assertEqual(get_user_model().objects.all()[0].username,self.username)
       self.assertEqual(get_user_model().objects.all()[0].email,self.email)


   