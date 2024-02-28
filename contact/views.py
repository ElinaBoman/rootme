from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ContactForm
from checkout.models import Order


# Create your views here.

def contact_view(request):
    """
    View to return contact.html
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent, we will contact you shortly!')
        else:
            messages.error(request, 'Meessage failed, make sure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
         'on_contact_view': True,
    }
    return render(request, 'contact/contact.html', context)
