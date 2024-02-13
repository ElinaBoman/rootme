from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    View to return products_detail.html
    """
    product = get_object_or_404(Product, pk=product_id)
    #Context sends data stored in product key to template products.html
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
