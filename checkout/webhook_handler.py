from django.http import HttpResponse
from .models import Order, OrderLineItem
from .products import Product
import json
import time

class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = stripe_charge.billing_details 
        shipping_details = intent.shipping
        total_sum = round(stripe_charge.amount / 100, 2) 

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    user_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    mobile_number__iexact=shipping_details.mobile_number,
                    country__iexact=shipping_details.country,
                    postalcode__iexact=shipping_details.postalcode,
                    city__iexact=shipping_details.city,
                    street_address1__iexact=shipping_details.street_address1,
                    street_address2__iexact=shipping_details.street_address2,
                    county__iexact=shipping_details.state,
                    total_sum__iexact=shipping_details.total_sum,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
            if order_exists:
                return HttpResponse(
                    content=f'Unhandled webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200)
            else:
                order = None
                try:
                    order = Order.objects.create(
                        user_name=shipping_details.name,
                        email=shipping_details.email,
                        mobile_number=shipping_details.mobile_number,
                        country=shipping_details.country,
                        postalcode=shipping_details.postalcode,
                        city=shipping_details.city,
                        street_address1=shipping_details.street_address1,
                        street_address2=shipping_details.street_address2,
                        county=shipping_details.state,
                        original_basket=basket,
                        stripe_pid=pid,
                    )
                    for item_id, item_data in json.loads(basket).items():
                        product = Product.objects.get(id=item_id)
                        if isinstance(item_data, int):
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                            )
                            order_line_item.save()
                    
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Exception as e:
                    if order:
                        order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} | ERROR: {e}',
                        status=500)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                status=200)
            
            

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
