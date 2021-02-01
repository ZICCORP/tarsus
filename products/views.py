
from django.views.generic import ListView,DetailView

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

from .models import Product


class ProductListView(LoginRequiredMixin,ListView):

    model =  Product
    template_name ='products/product_list.html'
    login_url = 'account_login'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    login_url = 'account_login'
    permission_required = 'products.special_status'