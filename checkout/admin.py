from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_id', 'date',
                       'delivery_fee', 'order_total',
                       'total_sum', 'original_basket',
                       'stripe_pid')
    fields = ('order_id', 'date', 'user_profile', 'user_name', 'email',
              'mobile_number', 'country', 'postalcode', 'city',
              'street_address1', 'street_address2', 'county',
              'delivery_fee', 'order_total', 'total_sum',
              'original_basket', 'stripe_pid')
    list_display = ('order_id', 'date', 'user_name',
                    'order_total', 'delivery_fee',
                    'total_sum')
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
