from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_category = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')


    def __str__(self):
        return self.product_name
