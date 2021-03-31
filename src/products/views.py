from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404
# Create your views here.

class ProductListView(ListView):
  queryset = Product.objects.all()
  template_name = "products/list.html"

  # def get_context_data(self, *args, **kwargs):
  #   context = super(ProductListView, self).get_context_data(*args, **kwargs)
  #   print(context)
  #   return context

def product_list_view(request):
  queryset = Product.objects.all()
  context = {
    'object_list': queryset
  }
  print(queryset)
  return render (request, "products/list.html", context) 


class ProductDetailSlugView(DetailView):
  queryset = Product.objects.all()
  template_name = "products/detail.view"

  def get_object(self, *args, **kwargs):
    request = self.request
    instance = get_object_or_404(Product, slug=self.kwargs.get('slug'))
    try:
      instance = Product.objects.get(slug=self.kwargs.get('slug'))
    except Product.DoesNotExist:
      raise Http404("Not found")
    except Product.MultipleObjectsReturned:
      return Product.objects.filter(slug=self.kwargs.get('slug')).first()

class ProductDetailView(DetailView):
  print("hello world")
  queryset = Product.objects.all()
  template_name = "products/detail.html"

  # def get_context_data(self, *args, **kwargs):
  #   context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
  #   print(context)
  #   return context

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


