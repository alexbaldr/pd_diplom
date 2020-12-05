from rest_framework import serializers
from rest_framework.relations import RelatedField
from shop.models import *
from shop.models import Shop
from registration.models import User


class ShopSerializers(serializers.ModelSerializer):
    shop_manager = serializers.StringRelatedField(read_only=True)
    shop_manager_id = serializers.IntegerField()
    class Meta:
        model = Shop
        fields = ('id', 'name', 'url', 'file',
                  "shop_manager", 'shop_manager_id')


class CategorySerializers(serializers.ModelSerializer):
    shop_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'shop_id',)


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"#('id', 'name', 'category',)


class ProductInfoSerializers(serializers.ModelSerializer):
    product_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Productinfo
        fields = ('id', 'name', 'shop', "product", 'product_id', 'quantity', 'price', 'price_rrc')


class ParameterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ('id', 'name',)


class OrderSerializers(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Order
        fields = ('user', 'dt', 'user_id', )


class OrderItemSerializers(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    shop = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField()
    shop_id = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ('order', 'product', 'shop', 'quantity', 'shop_id', 'product_id',)


class ContactSerializers(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Contact
        fields = ('id', 'city', 'address', 'phone', 'user_id',)
