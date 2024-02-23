from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user_name', 'email', 'mobile_number',
                  'street_address1', 'street_address2',
                  'city', 'postalcode', 'country', 'county',)
    
    def __init__(self, *args, **kwargs):
        """
        Overriding auto generated labels and
        adding placeholders and classes.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_name': 'Full Name',
            'email': 'Email Address',
            'mobile_number': 'Phone Number',
            'postalcode': 'Postal Code',
            'city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['user_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False 