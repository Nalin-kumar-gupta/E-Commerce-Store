from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    
]

