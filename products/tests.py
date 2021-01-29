from django.test import TestCase,Client

from django.urls import reverse

from .models import Product


class ProductTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(title="Laptop",seller='okenny john',price='29.99')


    def test_product_listing(self):
        self.assertEqual(f'{self.product.title}','Laptop')
        self.assertEqual(f'{self.product.seller}','okenny john')
        self.assertEqual(f'{self.product.price}','29.99')

    def test_product_list_view(self):
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Laptop")
        self.assertTemplateUsed(response,'products/product_list.html')

    def test_product_detail_view(self):
        response = self.client.get(self.product.get_absolute_url())
        no_response = self.client.get('/products/12345/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,"Laptop")
        self.assertTemplateUsed(response,'products/product_detail.html')
