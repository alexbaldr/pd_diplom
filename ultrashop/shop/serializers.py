from rest_framework_jwt import serializers
from ultrashop.shop.models import Shop

class ShopSerializers(serializers.ModelSerializers):
    class Meta:
        model = Shop