"""component URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from product.views import product_list_view, component, product_detail_view
from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView
from .views import home_page, login_page, register_page

urlpatterns = [
    url(r'^login/$', login_page, name='login'),
    url(r'^register/$', register_page, name='register'),
    url(r'^product/$', product_list_view, name='product'),
    url(r'^component/$', component, name='component'),

    url(r'^cart/', include(('cart.urls', 'cart'), namespace='cart')),
    #url(r'^detail/$', product_detail_view, name='detail'),
    #url(r'^product/product-(?P<parameter>[\w-]+).html', 'views.product', name="product"),
    #url(r'^stores/\w+/',.....)
    url(r'^detail/(?P<parameter>[\w-]+)/$', product_detail_view, name='detail'),
    url(r'^$', home_page, name='home'),
    url(r'^admin/', admin.site.urls),

]
