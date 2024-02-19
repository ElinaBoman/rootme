from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from products.models import Product



def view_basket(request):
    """
    View to return basket.html
    """

    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """Add products to shopping basket"""
    print(Product)
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {product.name} to basket')
    request.session['basket'] = basket

    return redirect(redirect_url)


def adjust_basket(request, item_id):
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)
    request.session['basket'] = basket
    return redirect(reverse('view_basket'))



def remove_from_basket(request, item_id):
    try:
        basket = request.session.get('basket', {})
        basket.pop(item_id)
        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)



