from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from products.models import Product

class SearchProductListView(ListView):
  template_name = "search/view.html"

  # def get_context_data(self, *args, **kwargs):
  #   context = super(ProductListView, self).get_context_data(*args, **kwargs)
  #   print(context)
  #   return context

# This function is overriden function
# It is used for searching and filtering purpose based on the given parameter
  def get_queryset(self, *args, **kwargs):
    request = self.request
    # get query parameter
    query = request.GET.get('q')
    # check if user has selected sort by name radio button
    sort_by_name = request.GET.get('name-sort')

    # check if user has selected sort by pricce radio button
    sort_by_price = request.GET.get('price-sort')
    print(sort_by_name, sort_by_price)
    #  if query is set check whether the user has selected radio buttons or not or not
    if query is not None:
      products = Product.objects.filter(title__icontains=query)
      if sort_by_name is not None and sort_by_price is not None:
        products = products.order_by('title', 'price')
      elif sort_by_price is None:
        products = products.order_by('-price')
      elif sort_by_name is None:
        products = products.order_by('title')

      return products
   
    return Product.objects.all()
