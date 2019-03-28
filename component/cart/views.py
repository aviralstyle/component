from django.shortcuts import render, redirect

# Create your views here.
from .models import Cart
from product.models import Product

#def cart_create(user=None):  #default method
#    cart_obj = Cart.objects.create(user=None)
#    print("new cart created")
#    return cart_obj

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print("2")
    print(new_obj)
    return render(request, "cart/home.html", {"cart": cart_obj})


def cart_update(request):
    print(request.POST)
    product_id=request.POST.get('product')
    product_obj=Product.objects.get(id = product_id)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    #print (new_obj)
    cart_obj.product.add(product_obj)
    print("3")
    current_user = request.user
    print(current_user.id)
    Product.objects.filter(id=product_id).update(status='IN USE')
    return redirect("cart:home")
