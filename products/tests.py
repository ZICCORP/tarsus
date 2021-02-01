from django.test import TestCase,Client

from django.urls import reverse

from .models import Product,Review

from django.contrib.auth.models import Permission

from django.contrib.auth import get_user_model


class ProductTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='reviewuser',email='reviewuser@email.com',password='frank123')
        self.product = Product.objects.create(title="Laptop",seller='okenny john',price='29.99')
        self.review = Review.objects.create(seller=self.user,product=self.product,review='absolutely loved it')
        self.special_permission = Permission.objects.get(codename='special_status')


    def test_product_listing(self):
        self.assertEqual(f'{self.product.title}','Laptop')
        self.assertEqual(f'{self.product.seller}','okenny john')
        self.assertEqual(f'{self.product.price}','29.99')

    def test_product_list_view_for_login_user(self):
        self.client.login(email='reviewuser@email.com',password='frank123')
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Laptop")
        self.assertTemplateUsed(response,'products/product_list.html')

    def test_product_list_view_for_logout_user(self):
        self.client.logout()
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code,302)
        self.assertRedirects(response,'%s?next=/products/' % (reverse('account_login')))
        response = self.client.get('%s?next=/products/' % (reverse('account_login')))
        self.assertContains(response,'Log In')

    def test_product_detail_view_with_permission(self):
        self.client.login(email='reviewuser@email.com',password='frank123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/products/12345/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,"Laptop")
        self.assertContains(response,'absolutely loved it')
        self.assertTemplateUsed(response,'products/product_detail.html')
