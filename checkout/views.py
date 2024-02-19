from django.shortcuts import render


def checkout(request):
    """
    View to return index.html
    """
    return render(request, 'checkout/checkout.html')
