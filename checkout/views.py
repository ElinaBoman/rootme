from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    """
    View to return checkout.html
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There are no products in you basket")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "pk_test_51OgS3vBh7I7U1kIQRspo5HR4EUuWS9Jxe7SApxGXgFuo1ISs4EVFCh8O1ZM3sC6E9CeAm2sivePvE3nF7om2GCn500vde772Vx",
        'client_secret': 'test client secret', 
    }

    return render(request, template, context)