from django.urls import path
from . import views

urlpatterns = [

    path('', views.store, name="store"),
    path('timber/', views.timber, name="timber"),
    path('hotel/', views.hotel, name="hotel"),
    path('cart/', views.cart, name="cart"),
    path('search/', views.search, name="search"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),


    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]
