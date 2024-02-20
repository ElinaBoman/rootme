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
    }

    return render(request, template, context)