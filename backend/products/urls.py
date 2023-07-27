from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductRetrieveUpdateView.as_view()),
    path('', views.ProductListView.as_view()),
    path('create/', views.ProductCreateView.as_view()),
    path('<int:pk>/update/', views.ProductRetrieveUpdateView.as_view()),
    path('<int:pk>/destroy/', views.ProductRetrieveDestroyView.as_view()),
]