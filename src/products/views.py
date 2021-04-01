from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404
from carts.views import get_cart
# Create your views here.

class ProductListView(ListView):
  queryset = Product.objects.all()
  template_name = "products/list.html"
  
  def get_context_data(self, *args, **kwargs):
    cart_obj = get_cart(self.request)

    context = super(ProductListView,self).get_context_data(*args, **kwargs)
    context['cart'] = cart_obj
    print(cart_obj)
    return context
# 
# This class is used to show the details of each product 
# It inherits the built-in DetailView classes
class ProductDetailView(DetailView):
  # Get all products
  queryset = Product.objects.all()
  template_name = "products/detail.html"

  def get_context_data(self, *args, **kwargs):
    cart_obj = get_cart(self.request)
    context = super(ProductDetailView,self).get_context_data(*args, **kwargs)
    # Pass the cart the products in to the context
    # so that it can be used if user is not authenticated during adding to cart
    context['cart'] = cart_obj
    return context