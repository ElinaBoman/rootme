from decimal import Decimal
from django.conf import settings
"""
    Context processor this is avaiable because it's
    added to templates inside context_processors in settings.py. 
    The contexts is similar to other contexts in other views,
     but this one is avaiable because it's added inside settings.py.
"""
def basket_contents(request):
    basket_products = []
    total = 0
    product_count = 0
    total_sum = 0

    
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery = 0

        total_sum = delivery + total
        
    context = {
        'basket_contents': basket_contents,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery': free_delivery,
        'free_delivery_threshold' : settings.FREE_DELIVERY_THRESHOLD,
        'total_sum' : total_sum
    }

    return context 

