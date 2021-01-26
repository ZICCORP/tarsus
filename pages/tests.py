from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import HomePageView,AboutPageView

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

class AboutPageTest(SimpleTestCase):

    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code,200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response,'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response,'My About Page')

    def test_aboutpage_contains_incorrect_html(self):
        self.assertNotContains(self.response,'Hello Africa')

    def test_aboutpage_url_resolves_aboutpageView(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__,AboutPageView.as_view().__name__)
    

