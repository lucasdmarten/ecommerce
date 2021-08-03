from django.contrib import admin

from store.models import *


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user','name', 
    'email']
admin.site.register(Customer, CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer','complete', 
    'transaction_id',
    'get_cart_quantity', 'get_cart_total', 'get_cart_items']
admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'product','order', 'quantity',
    'get_price', 'get_total', 
    'date_add', 'complete', 'transaction_id']
admin.site.register(OrderItem, OrderItemAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description', 'price', 'slug', 
    'created_at', 'imageURL']
admin.site.register(Product, ProductAdmin)

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['customer','order', 'address',
    'city', 'state',  'zipcode', 'date_add',
    'complete', 'transaction_id' ]
admin.site.register(ShippingAddress, ShippingAddressAdmin)
