from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(request):
    desktop_products = Product.objects.filter(
        category__name='desktop_pc'
    )

    laptop_products = Product.objects.filter(
        category__name='laptops'
    ) 

    mobile_products = Product.objects.filter(
        category__name='mobile_devices'
    ) 
    
    context = {
        'desktop_products': desktop_products,
        'laptop_products': laptop_products,
        'mobile_products': mobile_products,
    }

    return render (request, 'home/index.html', context)
