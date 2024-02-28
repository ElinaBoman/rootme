from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ContactForm
from contact.models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings



# Create your views here.
def _send_confirmation_email():
    """Send confirmation email to customer"""
    customer_email = Contact.contact_email
    subject = 'Q&A'
    body = 'Thank you for reaching out, we will be in contact with you shortly!\nBest regards,\nRoot|Me'
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email]
    )


def contact_view(request):
    """
    View to return contact.html
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent, we will contact you shortly!')
            _send_confirmation_email()
            return redirect('contact_view')

        else:
            messages.error(request, 'Message failed, make sure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
        'on_contact_view': True,
    }
    return render(request, 'contact/contact.html', context)


