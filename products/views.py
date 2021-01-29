
from django.views.generic import ListView,DetailView

from .models import Product


class ProductListView(ListView):

    model =  Product
    template_name ='products/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'