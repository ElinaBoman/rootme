from django.db import models
from profiles.models import UserProfile
from products.models import Product


class WishList(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                             null=False, blank=False,
                             related_name='user_wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wish_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.product.name
