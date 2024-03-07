from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404)
from .models import WishList
from products.models import Product
from profiles.models import UserProfile
from django.contrib import messages


def wishlist_view(request):
    """"
    View to render wishlist
    """
    user_profile = UserProfile.objects.get(user=request.user)
    user_wishlist = WishList.objects.filter(user=user_profile)
    print('request', request.user)
    context = {
        'user_wishlist': user_wishlist
    }
    print('userwish', user_wishlist)
    template = 'wishlist/wishlist.html'
    return render(request, template, context)


def add_product_to_wishlist(request, product_id):
    """
    Add product to Wishlist
    """
    wish_product = get_object_or_404(Product, pk=product_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if WishList.objects.filter(user=user_profile,
                               product=wish_product).exists():
        messages.error(request, f'Product {wish_product.name} \
                       already exists in your wishlist!')
    else:
        wishlist_item = WishList.objects.create(
            user=user_profile,
            product=wish_product
        )
        messages.success(request, f'Product {wishlist_item.product.name} \
                         has been added to wishlist successfully!')
    return redirect(reverse('products'))


def delete_product_from_wishlist(request, product_id):
    """
    Delete product from Wishlist
    """
    user_profile = UserProfile.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = WishList.objects.get(user=user_profile, product=product)
    wishlist_item.delete()
    messages.success(request, f' {product.name} \
                     has been removed from wishlist!')
    return redirect('wishlist_view')
