from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=300, null=True, blank=True)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    """
    Product class for all produkts
    """
    POT_SIZE = (
        ('7cm', '7cm'),
        ('14cm', '14cm'),
        ('24cm', '24cm'),
        ('40cm', '40cm'),
        ('54cm', '54cm'),

    )
    OPTION_CURRENT_STADGE = (
        ('Ready to be planted', 'Ready to be planted'),
        ('Not ready be planted', 'Not ready to be planted'),
        ('Has been planted', 'Has been planted'),
    )

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    pot_size = models.TextField(max_length=10, choices=POT_SIZE, null=True, blank=True)
    current_stadge = models.CharField(max_length=300, choices=OPTION_CURRENT_STADGE, null=True, blank=True)
    image_url = models.URLField(max_length=1200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
