from django.shortcuts import render, redirect

# Create your views here.
from .models import Cart
from product.models import Product
from tracker.models import Tracker
from datetime import datetime
#def cart_create(user=None):  #default method
#    cart_obj = Cart.objects.create(user=None)
#    print("new cart created")
#    return cart_obj

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "cart/home.html", {"cart": cart_obj})


def cart_update(request):
    print(request.POST)
    product_id=request.POST.get('product')
    product_obj=Product.objects.get(id = product_id)
    current_user = request.user
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    #t_obj, new_obj = Tracker.objects.new_or_exist(request)

    #print (new_obj)
    if product_obj in cart_obj.product.all():
        cart_obj.product.remove(product_obj)
        Product.objects.filter(id=product_id).update(status='FREE', uid=0)
        Tracker.objects.filter(user=current_user).filter(product=product_obj).update(removed=datetime.now())
    else:
        cart_obj.product.add(product_obj)
        Product.objects.filter(id=product_id).update(status='IN USE', uid=current_user.id)
        x=Tracker.objects.new(user=current_user, product=product_obj)
        x.accessed=datetime.now()
    return redirect("cart:home")
