from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('create/', views.postData),
    path('<int:pk>/', views.get_product_detail),
]
