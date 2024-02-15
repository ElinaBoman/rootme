from django.shortcuts import render


def index(request):
    """
    View to return index.html
    """
    return render(request, 'home/index.html')