import json
from shop.serializers import ShopSerializers, ParameterSerializers
from django.test import TestCase, client
from django.urls import reverse
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from shop.models import Parameter, Shop

class PostShopTest(APITestCase):
    def test_get_all_shops(self):
        client = APIClient()
        response = client.post('/api/v1/shops/', {"name": 'Avito'}, format='json')
        print(response.content)
        self.assertEqual(response.status_code, 200)


class ShopTestCase(APITestCase):
    def test_get_shops(self):
        response = self.client.get('/api/v1/shops/')
        print(response.content)
        self.assertEqual(response.status_code, 200)


# class LoginTest(APITestCase):
#     def test_for_login(self):
#         client = APIClient()
#         response = client.login(username='admin', password='admin')
#         print(response)
#         self.assertEqual(response, False)

# class ProductTestCase(APITestCase):
#     def test_get_products(self):
#         response = self.client.get('/api/v1/products/')
#         print(response.content)
#         self.assertEqual(response.status_code, 200)

# class GetShopTest(APITestCase):
#     def setUp(self):
#         self.valid_payload = {'name':"weight"}

#     def test_create_valid(self):
#         response = self.client.post(
#             'api/v1/products/product/parametr/',
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         print(response.content)
#         self.assertEqual(response.status_code, 201)

#     def test_create_invalid_puppy(self):
#         response = self.client.post(
#             'api/v1/products/product/parametr/',
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json'
#         )
#         print(response.content)
#         self.assertEqual(response.status_code, 400)
