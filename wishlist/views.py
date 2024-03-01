from django.shortcuts import render, redirect, reverse,  HttpResponse, get_object_or_404
from .models import WishList
from products.models import Product
from django.contrib.auth.models import User

from django.contrib import messages

def wishlist_view(request):
    """"
    View to render wishlist
    """
    template = 'wishlist/wishlist.html'
    return render(request, 'wishlist/wishlist.html')

def add_product_to_wishlist(request, item_id):
    ''''
    View to add products to wishlist
    '''
    wishlist = Product.objects.get(pk=item_id)
    if request.method == 'POST':
        WishList.save()
        
    quantity = 0
    print('description', wishlist.description)
    print('wishlist', wishlist)



    return redirect('wishlist_view')


    

        



    
