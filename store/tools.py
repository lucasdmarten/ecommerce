import json

from accounts.models import *
from store.forms import *
from store.models import *


def get_data(request):
    user = request.user
    products = Product.objects.all()
    myuser = MyUser.objects.filter(email=user.email)[0]
    customer, created = Customer.objects.get_or_create(user=myuser,
                    name=user.username,email=user.email)
    order, created = Order.objects.get_or_create(customer=customer,
                                                complete=False)
    orderitems = order.orderitem_set.all()
    quantity = order.get_cart_quantity
    # try:
    #     orderitem = OrderItem.objects.get(
    #                 order=order,product=product) 
    # except:
    #     orderitem = OrderItem.objects.create(
    #                 order=order,product=product)

    context = dict(products=products, order=order,
            orderitems=orderitems, 
            customer=customer, quantity=quantity)
    return context