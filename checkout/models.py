from django.db import models
import uuid
from django.conf import settings
from django.db.models import Sum

from products.models import Product


class Order(models.Model):
    order_id = models.CharField(max_length=32, null=False, editable=False)
    user_name = models.CharField(max_length=60, null=False, blank=False)
    email = models.EmailField(max_length=60, null=False, blank=False)
    mobile_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=30, null=False, blank=False)
    postalcode = models.CharField(max_length=30, null=False, blank=False)
    city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, blank=True, null=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_fee = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_id(self):
        """
        Create a random and uniqe order number.
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
            Override save method if no order_id
            has been created, generates order number by calling
            _generate_order_id()
        """
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.order_id

    def update_total(self):
        """
        Update total_sum when a new line item is added,
        calc with delivery cost.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_fee = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_fee = 0
        self.total_sum = self.order_total + self.delivery_fee
        self.save()


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)


    def save(self, *args, **kwargs):
        """
            Override save method if no order_id
            has been created, generates order number by calling
            _generate_order_id()
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_id}'



