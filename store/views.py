import datetime
import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from accounts.models import *
from store import tools
from store.forms import *
from store.models import *


def index(request):
    user = request.user
    if user.is_authenticated:
        context = tools.get_data(request)
        return render(request, 'store/home.html', context)
    else:
        products = Product.objects.all()
        context = dict(products=products)
        return render(request, 'store/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = tools.get_data(request)
    context['product'] = product
    return render(request, 'store/product.html', context)


def update_order(request):

    if request.method == "POST":
        d = json.loads(request.body)
        productId, action = d['productId'], d['action']
        product=Product.objects.get(id=productId)
        context = tools.get_data(request) 
        order = context['order']

        # ALWAYS RETURN MORE THAN ONE OBJECTS
        # orderitem, created = OrderItem.objects.get_or_create(
        #     order=order, product=product
        # )
        # SOLUTION:
        try:
            orderitem = OrderItem.objects.get(
                        order=order,product=product) 
        except:
            orderitem = OrderItem(
                        order=order,product=product)
        ##############################################
         
        if action == 'add':  
            orderitem.add
        elif action == 'remove':
            orderitem.remove
        orderitem.save()
        if orderitem.quantity == 0:
            orderitem.delete()         
        return redirect('cart')

    else:
        return redirect('store')
    

def cart(request):
    print('cart page')
    products = Product.objects.all()
    user = request.user
    if user.is_authenticated:
        context = tools.get_data(request)
        return render(request, 'store/cart.html', context=context)
    
    else:
        context = dict(products=products)
        print('render..')
        return render(request, 'store/cart.html', context=context)


def checkout(request):
    user = request.user
    if user.is_authenticated == False:
        return redirect('register')
    context = tools.get_data(request)
    print('checkout')
    print(request.method)
    if request.method=="POST":
        print('POST')
        print('body ', request.POST)
        form = UserInformation(data=request.POST)
        if form.is_valid():
            shipping = form.save(context['customer'], context['order'])
            print(shipping)
            context['shipping'] = shipping
            return render(request, 'store/pay_button.html', context=context)
        
    else:
        form = UserInformation()
        context['form'] = form
        return render(request, 'store/checkout.html', context=context)

  
def payment_button(request):

    transaction_id = datetime.datetime.now().timestamp()

    if request.method == "POST":
        payment = json.loads(request.body)

        if payment:
            context = tools.get_data(request)
            order = context['order']
            order.complete = True
            order.transaction_id = transaction_id
            order.save()

    return JsonResponse({
        "message": "Congratulations",
        "order": context['order'].complete
    })