
from rest_framework import response
from shop.serializers import ShopSerializers
from django.test import TestCase, client
from django.urls import reverse

from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from shop.models import Shop

# client = APIClient()
# client.post('/shops/', {"name": 'Avito'}, format='json')

# client = APIClient()
# client.login(username='admin', password='admin')
# client.logout()

# class GetShopTest(TestCase):
#     def setUp(self):
#         self.casper = Shop.objects.create(
#                                             name= "Second Shop",
#                                             url= "https://www.avto.ru",
#                                             shop_manager_id= 1,
#                                             )
#     def test_get_all_shops(self):
#         response = client.get(reverse('shops'))
#         shop = Shop.objects.all()
#         serializer = ShopSerializers(shop, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


class ShopTestCase(APITestCase):
    def test_get_shops(self):
        response = self.client.get('/api/v1/shops/')
        self.assertEqual(response.status_code, 200)
