from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from .forms import OrderForm
from basket.contexts import basket_contents
from django.conf import settings
import stripe
import os
if os.path.exists("env.py"):
  import env


def checkout(request):
    """
    View to return checkout.html
    """
    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    stripe_secret_key = os.environ.get('STRIPE_SECRET_KEY')

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There are no products in you basket")
        return redirect(reverse('products'))
    
    current_basket = basket_contents(request)
    total = current_basket['total_sum']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    
    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)