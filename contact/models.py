from django.db import models
import datetime

# Create your models here.

class Contact(models.Model):
    contact_email = models.EmailField(max_length=60, null=False, blank=False)
    contact_date = models.DateField(auto_now_add=True, null=True)
    contact_subject = models.CharField(max_length=30, null=False, blank=False)
    contact_message = models.TextField(max_length=500, null=False, blank=False)