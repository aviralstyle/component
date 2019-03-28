from django.views.generic import ListView
from .models import Product
from django.shortcuts import render

from cart.models import Cart
# Create your views here.

def component(request):
    queryset = Product.prod_choice
    #queryset = Product._meta.get_field('type').choices
    context = {
        'object_list' : queryset
    }
    return render(request, "product/component.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request, "product/list.html", context)


def product_detail_view(request, parameter):

#    instance = Product.objects.get(type=i)
    queryset = Product.objects.filter(type=parameter)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    current_user = int(request.user.id)
    #print (current_user)
    context = {
        'object_list' : queryset,
        'cart'        : cart_obj,
        'userid'      : current_user,
    }
    return render(request, "product/detail.html", context)
