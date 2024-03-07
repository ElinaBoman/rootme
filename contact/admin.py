from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):

    fields = (
        'contact_email',
        'contact_subject',
        'contact_message'
    )

    list_display = (
        'contact_email',
        'contact_subject',
        'contact_message',
        'contact_date',
    )


admin.site.register(Contact, ContactAdmin)
