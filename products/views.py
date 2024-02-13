from django.shortcuts import render
from .models import Product

def all_products(request):
    """
    View to return products.html
    """
    products = Product.objects.all()
    #Context sends data stored in product key to template products.html
    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
