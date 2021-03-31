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
   

def product_list_view(request):
  queryset = Product.objects.all()
  context = {
    'object_list': queryset
  }
  return render (request, "products/list.html", context) 

class ProductDetailView(DetailView):
  print("hello world")
  queryset = Product.objects.all()
  template_name = "products/detail.html"

  def get_context_data(self, *args, **kwargs):
    cart_obj = get_cart(self.request)
    context = super(ProductDetailView,self).get_context_data(*args, **kwargs)
    context['cart'] = cart_obj
    return context
   

def product_detail_view(request, pk=None, *args, **kwargs):
  # instance = Product.objects.get(pk=pk)
  instance = Product.objects.get_by_id(pk)
  if instance is None:
    raise Http404("Product does not exist")
  instance = get_object_or_404(Product, pk=pk)
  queryset = Product.objects.all()
  context = {
    'object': instance
  }
  print(queryset)
  return render (request, "products/detail.html", context) 


