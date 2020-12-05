from shop.models import *
from django.contrib import admin


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    list_filter = ['state', ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category', 'slug', ]
    list_filter = ['state', ]


@admin.register(Productinfo)
class ProductinfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'shop', 'product', 'quantity', 'price', 'price_rrc', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'dt', 'state', ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'shop', 'quantity', ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'address', 'phone', ]
