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

    tablet_products = Product.objects.filter(
        category__name='tablets'
    ) [:1]
    
    console_products = Product.objects.filter(
        category__name='gaming_consoles'
    ) [:1]

    accessory_products = Product.objects.filter(
        category__name='accessories'
    ) [:1]

    featured_products = list(
        chain(
           desktop_products,
           laptop_products,
           mobile_products, 
        )
    )

    featured_products_right = list(
        chain(
           tablet_products,
           console_products,
           accessory_products, 
        )
    )
    context = {
        'desktop_products': desktop_products,
        'laptop_products': laptop_products,
        'mobile_products': mobile_products,
        'featured_products': featured_products,
        'featured_products_right': featured_products_right,

    }

    return render (request, 'home/index.html', context)
