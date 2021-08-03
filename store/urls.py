from django.contrib import admin
from django.urls import path

from store import views

# app_name = 'store'

urlpatterns = [
    path('', views.index, name='store'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('update_order/', views.update_order, name='update_order'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment_button/', views.payment_button, name='payment_button'),
]

