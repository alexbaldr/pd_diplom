from django.urls import path
from . import views


urlpatterns = [
    path('shops/', views.ShopView.as_view(), name="shops"),
    path('products/', views.ProductView.as_view()),
    path('order/', views.OrderView.as_view()),
    # path('shops/<int:slug>/', ShopDetailView.as_view()),
    path('shops/shop/', views.ShopDetailView.as_view({'get': 'list'})),
    path('products/product/', views.ProductDetailView.as_view()),
    path('products/product/<int:pk>/', views.ChangeProductView.as_view()),
    path("products/product/parametr/", views.ParametrView.as_view({'get': 'list', })),
    path('user/contacts/', views.ContactView.as_view({'get': 'list',
                                                      'post': 'create'})),
    path('user/contacts/<pk>', views.ContactView.as_view({'get': 'retrieve',
                                                          'delete': 'destroy',
                                                          'put': 'update', }),
                                                          name='contact_detail'),
    path('shops/category/', views.CategoryView.as_view(), name='category'),
]
