from django.db import models
from django.conf import settings
# Create your models here.
from product.models import Product

User = settings.AUTH_USER_MODEL

class CompManager(models.Manager):
    def new_or_get(self, request):
        comp_id = request.session.get("comp_id", None)
        crtid   = request.user.id
        qs = self.get_queryset().filter(crtid=request.user.id)
        if qs.count() == 1:
            new_obj = False
            #print("cart id exist")
            comp_obj = qs.first()

            if request.user.is_authenticated and comp_obj.user is None:
                comp_obj.user = request.user
                comp_obj.save()
        else:
            comp_obj = Comp.objects.new(user=request.user)
            new_obj = True
            request.session['comp_id'] = comp_obj.id

        return comp_obj, new_obj

    def new(self, user=None):
        print (user)
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user = user_obj)

class Comp(models.Model):
    crtid       = models.CharField(max_length=20, blank=False)
    user        = models.ForeignKey(User, null = True, blank=True, on_delete = models.CASCADE)
    product     = models.ManyToManyField(Product,blank=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    objects = CompManager()

    def __str__(self):
        return str(self.crtid)
