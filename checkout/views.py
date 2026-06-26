from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings
from basket.contexts import basket_contents
import stripe
from .models import Order, OrderLineItem
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request):
   
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There are no products in your basket")
        return redirect(reverse('products'))
    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    intent = stripe.PaymentIntent.create(
        amount=stripe_total, currency=settings.STRIPE_CURRENCY,
    )
    
    if request.method == 'POST':
        basket=request.session.get('basket', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number':request.POST['phone_number'],
            'country': request.POST['country'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
       
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order= order_form.save()
            
            for item_id, item_data in basket.items():
                product =get_object_or_404(Product, pk=item_id)

                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                )
                    order_line_item.save()
                request.session['save_info'] = 'save-info' in request.POST
                return redirect ( reverse('checkout_success', args=[order.order_number]))
        else:
                messages.error(request, 'An error with your form has occured, please double check you have inputted the correct information')
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    if not stripe_public_key:
        messages.warning( request,'Stripe public key missing, did you forget to set it in your environment?')
    client_secret = intent.client_secret
    context = {
        'order_form': order_form,
        'stripe_public_key':stripe_public_key,
        'client_secret': client_secret
        
    }
    return render(request, template, context)

def checkout_success(request, order_number):
    save_info = request.session.get('save_info')
    order=get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order was successful! Your order number is {order_number}.'
                      f'A confirmation email will be sent to {order.email}.')
    if 'basket' in request.session:  
        del request.session['basket']
    template='checkout/checkout_success.html'
    context = { 
    'order': order,
    }
    return render(request, template, context)