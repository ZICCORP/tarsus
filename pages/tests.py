from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import HomePageView

class HomePageTests(SimpleTestCase):
   
   def setUp(self):
       url = reverse('home')
       self.response = self.client.get(url)

   def test_homepage_status_code(self):
       self.assertEqual(self.response.status_code,200)

   def test_homepage_template(self):
       self.assertTemplateUsed(self.response,'home.html')

   def test_homepage_contains_correct_html(self):
        self.assertContains(self.response,'Home Page')

   def test_homepage_contains_incorrect_html(self):
        self.assertNotContains(self.response,'Barawo')

   def test_homepage_url_resolves_homepageView(self):
       view = resolve('/')
       self.assertEqual(view.func.__name__,HomePageView.as_view().__name__)

    

