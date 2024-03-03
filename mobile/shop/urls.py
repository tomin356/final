"""
URL configuration for mobile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views
app_name='shop'

urlpatterns = [
    path('',views.home,name='home'),
    path('category',views.category,name='category'),
    path('products/<p>',views.products,name='products'),
    path('viewmore/<p>',views.viewmore,name="viewmore"),
    path('sale',views.sale,name='sale'),
    path('search',views.search,name='search'),
    path('register',views.register,name='register'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('cart',views.cart,name='cart'),
    path('addtocart/<p>',views.addtocart,name="addtocart"),
    path('minusquantity/<p>',views.minusquantity,name="minusquantity"),
    path('deletequantity/<p>',views.deletequantity,name="deletequantity"),
    path('orderform/',views.orderform,name="orderform"),
    path('orderview/',views.orderview,name="orderview"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('contact/',views.contact,name="contact"),

]



