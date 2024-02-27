from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from checkout.models import Order


# Create your views here.

def contact_view(request):
    """
    View to return contact.html
    """
    if request.method == 'POST':
        form = ContactForm()
        if form.is_valid():
            form.save()
            messages.success(request, 'Yor message has been updated successfully')
        else:
            messages.error(request, 'Meessage failed, make sure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    #Context sends data stored in product key to template products.html
    context = {
        'form': form,
    }
    return render(request, 'contact/contact.html', context)