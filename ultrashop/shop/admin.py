from shop.models import Shop, Category, Product, Productinfo, Order, OrderItem, Contact, Parameter, ProductParameter
from django.contrib import admin


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    # list_display = ['name', 'slug', ]
    list_display = [field.name for field in Shop._meta.get_fields()
                    if field.name not in
                    {"productinfo", "orderitem", "categories"}
                    ]
    list_filter = ['state', ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug' ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category', 'slug', ]
    list_filter = ['state', ]


@admin.register(Productinfo)
class ProductinfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Productinfo._meta.get_fields()
                    if field.name not in {"productparameter", "orderitem"}]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.get_fields()
                    if field.name not in {"orderitem"}]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = list_display = [field.name for field in OrderItem._meta.get_fields()]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_id', 'user', 'city', 'address', 'phone', ]


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_display = ['name', ]


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ['product_info', "value", ]
