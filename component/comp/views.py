from django.shortcuts import render, redirect

# Create your views here.
from .models import Comp
from product.models import Product

#def cart_create(user=None):  #default method
#    cart_obj = Cart.objects.create(user=None)
#    print("new cart created")
#    return cart_obj

def comp_home(request):
    comp_obj, new_obj = Comp.objects.new_or_get(request)
    print("2")
    print(new_obj)
    return render(request, "comp/home.html", {"comp": comp_obj})


def comp_update(request):
    print(request.POST)
    product_id=request.POST.get('product')
    product_obj=Product.objects.get(id = product_id)
    comp_obj, new_obj = Comp.objects.new_or_get(request)
    #print (new_obj)
    comp_obj.product.add(product_obj)
    print("3")
    current_user = request.user
    #Product.objects.filter(id=product_id).update(uid=current_user.id, status='IN USE')
    return redirect("comp:home")
