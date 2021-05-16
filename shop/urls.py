from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path('categories/', views.viewByCategory, name="viewCategories"),
    path('contact/', views.contact, name="contact"),
    path('tracker/', views.tracker, name="tracker"),
    path('productView/<int:id>', views.productView, name="productView"),
    path('search/', views.search, name="search"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
    path('cancelOrder/', views.cancelOrder, name="cancelOrder"),
]