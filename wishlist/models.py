from django.db import models
from django.contrib.auth.models import User
from products.models import Product
import datetime

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wish_created = models.DateField(auto_now_add=True, null=True)

    print('product', product)