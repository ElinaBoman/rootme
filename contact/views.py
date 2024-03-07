from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def _send_confirmation_email(customer_email):
    """
    Send confirmation email to customer
    """
    subject = 'Q&A'
    body = 'Thank you for reaching out, we will be in \
            contact with you shortly!\n Best regards,\nRoot|Me'
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
        print('form', form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent, \
                             we will contact you shortly!')
            customer_email = form.cleaned_data['contact_email']
            _send_confirmation_email(customer_email)
            return redirect('contact_view')

        else:
            messages.error(request, 'Message failed, \
                           make sure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
        'on_contact_view': True,
    }
    return render(request, template, context)

