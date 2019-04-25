from django.db import models
from django.conf import settings
from product.models import Product
# Create your models here.
User = settings.AUTH_USER_MODEL

class TrackerManager(models.Manager):
    def new_or_exist(self,request,product=None):
        tid  = request.user.id
        t_id = request.user.id
        prod_obj = product
        qs = self.get_queryset().filter(product=prod_obj)
        if qs.count() == 1:
            new_obj = False
            #print("cart id exist")
            t_obj = qs.first()

            if request.user.is_authenticated and t_obj.user is None:
                t.user = request.user
                t_obj.save()

        else:
            #print("count=", qs.count())
            t_obj = Tracker.objects.new(user=request.user, product=None)
            new_obj = True

        return t_obj, new_obj



    def new(self, user=None, product=None):
        #print (user)
        user_obj=None
        prod=product
        if user is not None:
            if user.is_authenticated:
                user_obj = user
                t_id = user.id
        return self.model.objects.create(tid= t_id,user = user_obj, product=prod)


class Tracker(models.Model):
    tid          = models.IntegerField( default=0)
    user        = models.ForeignKey(User, null = True, blank=True, on_delete = models.CASCADE)
    product     = models.ForeignKey(Product,blank=True, null=True, on_delete = models.CASCADE)
    accessed    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    removed     = models.DateTimeField(auto_now_add=False, blank=True, null=True)

    objects = TrackerManager()

    def __str__(self):
        return str(self.user.username)
