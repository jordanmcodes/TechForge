from django.shortcuts import render
from products.models import Product
from itertools import chain 

# Create your views here.

def index(request):
    desktop_products = Product.objects.filter(
        category__name='desktop_pc'
    ) [:1]

    laptop_products = Product.objects.filter(
        category__name='laptops'
    ) [:1]

    mobile_products = Product.objects.filter(
        category__name='mobile_devices'
    ) [:1]
    
    featured_products = list(
        chain(
           desktop_products,
           laptop_products,
           mobile_products, 
        )
    )
    context = {
        'desktop_products': desktop_products,
        'laptop_products': laptop_products,
        'mobile_products': mobile_products,
        'featured_products': featured_products,
    }

    return render (request, 'home/index.html', context)
