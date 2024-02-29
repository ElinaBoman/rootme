from django.shortcuts import render, redirect, reverse,  HttpResponse, get_object_or_404
from .models import WishList
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
    wish_product = WishList.objects.get(pk=item_id)
    wishlist = request.session.get('wishlist', {})
    
    if item_id in wishlist:
        wishlist[item_id] += 1
        messages.success(request, f'Updated {wish_product.name} quantity to {wishlist[item_id]}')
    else:
        wishlist[item_id] = wishlist
        messages.success(request, f'Added {wish_product.name} to basket')
        print('wish', wish_product)
        request.session['wishlist'] = wishlist
        print('wishlist', wishlist)

    template = 'products/products.html' 
    return render(request, template)
    

        



    
