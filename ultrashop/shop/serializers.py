from rest_framework import serializers
from .models import Shop, Category, Product, Productinfo, Order, OrderItem,\
                    Contact, Parameter, ProductParameter


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
        fields = "__all__"


class ProductInfoSerializers(serializers.ModelSerializer):
    product_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Productinfo
        fields = ('id', 'name', 'shop', "product", 'product_id',
                  'quantity', 'price', 'price_rrc')


class ProductParameterSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductParameter
        fields = ('id', 'name', 'product_info')


class ParameterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ('parameter', 'value')


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
        fields = ('order', 'product', 'shop', 'quantity',
                  'shop_id', 'product_id',)


class ContactSerializers(serializers.ModelSerializer):
    # contact_id - айди для определения максимального допустим
    # числа контактов для записи. заполняется во фронт-энде
    user_id = serializers.IntegerField()
    contact_id = serializers.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = Contact
        fields = ('contact_id', 'city', 'address', 'phone', 'user_id',)

    def create(self, validated_data):
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.city = validated_data['city']
        instance.address = validated_data['address']
        instance.phone = validated_data['phone']
        instance.save()
        return instance
