from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
# Imports search query, q will fetch product that has search in either name or description.
from django.db.models import Q
from .models import Product, Category

def all_products(request):
    """
    View to return products.html
    """
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    #Context sends data stored in product key to template products.html
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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
