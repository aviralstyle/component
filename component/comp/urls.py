from django.conf.urls import url

from .views import (
        comp_home,
        comp_update,
)

urlpatterns = [
    url(r'^$', comp_home, name='home'),
    url(r'^update/$', comp_update, name='update'),
]
