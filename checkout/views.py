from django.shortcuts import (render, reverse, redirect,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import OrderForm
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from basket.contexts import basket_contents
from django.conf import settings
from .models import OrderLineItem, Order
from products.models import Product
import stripe
import json
import os
if os.path.exists("env.py"):
    import env


@require_POST
def cache_checkout_data(request):
    """"
    Store customer meta data. Basket is the products
    the customer has palced in the basket save_info
    for customer who chooses to save their info.
    This would be shipping and billing details.
    username is saved to store previous purchases realated to a customer
    """
    try:
        # Paymentintent id
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    View to return checkout.html
    handles checkout process. First we get the stipe keys.
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
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket.items():
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
                    messages.error(request, ("One of the products \
                                   in your basket wasn't found in our database \
                                   Please contact us for further assistance."))
                    order.delete()
                    return redirect(reverse('view_basket'))
            request.session['save_info'] = 'save-info' in request.POST
            save_info = request.session['save_info']
            return redirect(reverse('checkout_success', args=[order.order_id]))
        else:
            messages.error(request, 'There was an error with your form. \
                           Please check your information again.')
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

        # Try to prefill the form with saved information
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'user_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'mobile_number': profile.default_mobile_number,
                    'country': profile.default_country,
                    'postalcode': profile.default_postalcode,
                    'city': profile.default_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
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

def checkout_success(request, order_id):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_id=order_id)
    # Ties user profile to the order
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_mobile_number': order.mobile_number,
                'default_country': order.country,
                'default_postalcode': order.postalcode,
                'default_city': order.city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order has been successfully processed!\
        Your order number is {order_id}. A confirmation email \
        will be sent to {order.email}')

    if 'basket' in request.session:
        del request.session['basket']
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }


    return render(request, template, context)