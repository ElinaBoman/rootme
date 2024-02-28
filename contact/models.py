from django.db import models
import datetime





class Contact(models.Model):

    CATEGORY_CHOICES = {
        ("Plants", "Plants"),
        ("Shipping & Delivery", "Shipping & Delivery"),
        ("Other", "Other")
    }

    contact_email = models.EmailField(max_length=60, null=False, blank=False)
    contact_date = models.DateField(auto_now_add=True, null=True)
    contact_subject = models.CharField(max_length=30, choices=CATEGORY_CHOICES,
                                        null=False, blank=False)
    contact_message = models.TextField(max_length=500, null=False, blank=False)