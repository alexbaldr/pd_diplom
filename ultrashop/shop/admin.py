from shop.models import *
from django.contrib import admin

# Register your models here.
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['name', 'url', ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['name', 'shops', ]

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['name', 'category', ]
    
@admin.register(Productinfo)
class ProductinfoAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['name', 'shop', 'product', 'quantity', 'price', ]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['user', 'dt', 'status']    


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ['order', 'product', 'shop', 'quantity']    


 