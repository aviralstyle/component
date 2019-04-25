from django.db import models

# Create your models here.




class Product(models.Model):
    id              = models.CharField(max_length=20, primary_key=True, blank=False)

    uid             = models.IntegerField(max_length=20, default=0)

    name            = models.CharField(max_length=50)

    prod_choice     = (
            ('Laptops', 'Laptops'),
            ('Storage', 'storage'),
            ('Mobiles', 'Mobiles'),
            ('Fashion', 'Fashion'),
    )
    type            = models.CharField(max_length=12, choices=prod_choice, blank=True)

    status_choice   = (
            ('FREE', 'Free'),
            ('IN USE', 'In use'),
    )
    status          = models.CharField(max_length=12, choices=status_choice, default='Free')

    condition_choice = (
            ('USABLE', 'Usable'),
            ('FAULTY', 'faulty'),
    )
    condition       = models.CharField(max_length=12, choices=condition_choice, default='Usable')



    def __str__(self):
        return self.name
