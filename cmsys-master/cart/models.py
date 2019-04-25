from django.db import models
from django.conf import settings
# Create your models here.
from product.models import Product

User = settings.AUTH_USER_MODEL

class CartManager(models.Manager):
    def new_or_get(self, request):
        crtid = request.user.id
        #print("crtid= ",crtid)
        #print(crtid)

        cart_id = request.user.id
        #print("Cartid=",cart_id)
               #crtid   = request.user.id
        qs = self.get_queryset().filter(crtid=cart_id)
        if qs.count() == 1:
            new_obj = False
            #print("cart id exist")
            cart_obj = qs.first()

            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            #print("count=", qs.count())
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            #crtid = request.user.id

        return cart_obj, new_obj

    def new(self, user=None):
        print (user)
        user_obj=None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
                cart_id = user.id
        return self.model.objects.create(crtid= cart_id,user = user_obj)

class Cart(models.Model):
    crtid       = models.CharField(max_length=20, blank=False)
    user        = models.ForeignKey(User, null = True, blank=True, on_delete = models.CASCADE)
    product     = models.ManyToManyField(Product,blank=True, null=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)
