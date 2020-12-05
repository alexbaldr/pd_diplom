from django.urls import path
from rest_framework.serializers import as_serializer_error
from shop.views import *

urlpatterns = [
    path('shops/', ShopView.as_view()),
    path('products/', ProductView.as_view()),
    path('order/', OrderView.as_view()),
    path('shops/<int:slug>/', ShopDetailView.as_view()),
    path ('products/product/', ProductDetailView.as_view()),
    path ('products/product/<int:pk>/',ChangeProductView.as_view()),
    path ('user/contacts/', ContactView.as_view()),
    path('shops/category/', CategoryView.as_view()),
]
