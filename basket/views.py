from django.shortcuts import render


def view_basket(request):
    """
    View to return basket.html
    """

    return render(request, 'basket/basket.html')
