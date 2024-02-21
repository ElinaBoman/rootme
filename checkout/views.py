from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from basket.contexts import basket_contents
from django.conf import settings
from .models import OrderLineItem, Order
from products.models import Product
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

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'user_name': request.POST['user_name'],
            'email': request.POST['email'],
            'mobile_number': request.POST['mobile_number'],
            'country': request.POST['country'],
            'postalcode': request.POST['postalcode'],
            'city': request.POST['city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county']

        } 
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket_items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Product.DoesNotExist:
                    message.error(request,
                    ("One of the peoducts in your basket wasn't found in our database"
                     "Please contact us for further assistance."))
                    order.delete()
                    return redirect(reverse('view_basket'))

            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \ Please check your information again.')
    else:   
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

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order has been successfully processed!\
        Your order number is {order_number}. A confirmation email \
        will be sent to {order.email}')

    if 'basket' in request.session:
        del request.session['basket']
    
    template = checkout/checkout_success.html
    context = {
        'order': order,
    }

    return render(request, template, context)