from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ A view to return the basket page """

    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
        """add quantity of selected product to the basket"""
        pass