from django.shortcuts import render
from product.models import Product
# Create your views here.
from .models import Tracker
from django.contrib.auth.decorators import login_required

@login_required
def tracker(request):
    #user = Tracker.objects.filter(user=request.user)
    #t_obj, new_obj = Tracker.objects.new_or_exist(request)
    tr = Tracker.objects.all()
    current_user = request.user
    return render(request, "tracker/home.html", {"t":tr, "cu":current_user})
