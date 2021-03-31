
from django.shortcuts import render, redirect

from .models import Cart
from products.models import Product
from django.http import JsonResponse
def get_cart(request):
    cart_id = request.session.get("cart_id", None)
    cart_obj = None
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        cart_obj = qs.first()
        print(cart_obj)
        if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = Cart.objects.new(user=request.user)
        request.session['cart_id'] = cart_obj.id
    return cart_obj

def cart_home(request):
    cart_obj = get_cart(request)
    products = cart_obj.products.all()
    total = 0
    print(cart_obj)
    for x in products:
      total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save() 
    return render(request, "carts/home.html", {"cart":cart_obj})


def cart_update(request):
  product = Product.objects.get_by_id(request.POST.get('product_id'))
  product_id = product.id

  cart_obj = get_cart(request)
  if product in cart_obj.products.all():
    cart_obj.products.remove(product)
    added=False
  else:
    cart_obj.products.add(product)
    added= True

  request.session['cart_items'] = cart_obj.products.count()
  # if javascript is not disabled use this method
  if request.is_ajax():
    json_data = {
      "added": added,
      "count": cart_obj.products.count()
    }
    return JsonResponse(json_data)
  return redirect("carts:home")
  # cart_obj