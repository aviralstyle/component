from django.views.generic import ListView
from .models import Product
from django.shortcuts import render, redirect

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

#    product_obj=Product.objects.get(id = product_id)

def product_detail_view(request, parameter):

#    instance = Product.objects.get(type=i)
    sort_id=request.POST.get('sort')
    print(sort_id)

    if sort_id=='1':
        queryset= Product.objects.filter(type=parameter).order_by('name')
        print(queryset)
        print('1')
    elif sort_id=='2':
        queryset= Product.objects.filter(type=parameter).order_by('-name')
        print(queryset)
        print('2')
    elif sort_id=='3':
        queryset= Product.objects.filter(type=parameter).order_by('status')
        print(queryset)
        print('3')
    elif sort_id=='4':
        queryset= Product.objects.filter(type=parameter).order_by('-status')
        print(queryset)
        print('4')
    elif sort_id=='5':
        queryset= Product.objects.filter(type=parameter).order_by('condition')
        print(queryset)
        print('5')
    elif sort_id=='6':
        queryset= Product.objects.filter(type=parameter).order_by('-condition')
        print(queryset)
        print('6')
    else:
        queryset= Product.objects.filter(type=parameter)
        print(queryset)
        print('7')

    cart_obj, new_obj = Cart.objects.new_or_get(request)
    current_user = int(request.user.id)

    #print (current_user)
    context = {
        'tpe'         : parameter,
        'object_list' : queryset,
        'cart'        : cart_obj,
        'userid'      : current_user,
    }
    return render(request, "product/detail.html", context)
