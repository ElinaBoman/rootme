from django.shortcuts import render
from products.models import Product
from django.contrib import messages

def wishlist_view(request):
    """"
    View to render wishlist
    """
    template = 'wishlist/wishlist.html'
    return render(request, 'wishlist/wishlist.html')

def add_product_to_wishlist(request, item_id):
    wish_products = Product.objects.get(pk=item_id)
    template = 'wishlist/wishlist.html'
    return render(request, 'wishlist/wishlist.html')

    
