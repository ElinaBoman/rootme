from django.shortcuts import render, redirect, reverse,  HttpResponse, get_object_or_404
from .models import WishList
from products.models import Product
from profiles.models import UserProfile
from products.views import all_products
from django.contrib import messages

def wishlist_view(request):
    """"
    View to render wishlist
    """
    user_profile = UserProfile.objects.get(user=request.user)
    user_wishlist = WishList.objects.filter(user=user_profile)
    context = {
        'user_wishlist' : user_wishlist
    }
    print('userwish', user_wishlist)
    template = 'wishlist/wishlist.html'
    return render(request, template, context)


def add_product_to_wishlist(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)
    
    if WishList.objects.filter(user=user_profile, product=product).exists():
        messages.error(request, f'Product {product.name} already exists in your wishlist!')
    else:
        wishlist_item = WishList.objects.create(
            user=user_profile,
            product=product
        )
        messages.success(request,f'Product {wishlist_item.product.name} has been added to wishlist successfully!')
    return redirect(reverse('wishlist_view'))