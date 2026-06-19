from django.shortcuts import render, get_object_or_404

from .models import Product, Category
# Create your views here.

def all_products(request):
    """ a view to showcase all products """

    products = Product.objects.all()
    current_categories = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')

        products = products.filter(
            category__name__in=categories)
        
        current_categories = Category.objects.filter(
            name__in=categories)

    context = {
        'products': products,
        'current_categories': current_categories,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ a view to showcase individual products """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)