from shop.signals import new_order_reciver
from rest_framework import mixins
from rest_framework import viewsets, status
from django.db.models.query_utils import Q
from django_filters.rest_framework import DjangoFilterBackend
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from shop.models import *
from shop.serializers import *
from registration.models import User
from rest_framework.decorators import action

# class Get_ID(APIView):
#     def user_id(self, request):
#         if request.user.is_authenticated:
#             return request.user.id

class CategoryView(APIView):
    # Получаем  и создаем категорию
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, *args, **kwargs):
        quaryset = Category.objects.all()
        serializer = CategorySerializers(quaryset, many=True)
        return Response(serializer.data)


class ShopView(APIView):
    #  Создаем магазин и получаем все магазины
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = ShopSerializers(data={'name': request.data['name'],
                                               'url': request.data["url"],
                                               'shop_manager_id': request.user.id})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            return JsonResponse({'Status': False, 'Errors': 'Нужна регистрация пользователя'})

    def get(self, request, *args, **kwargs):
        quaryset = Shop.objects.all()
        serializer = ShopSerializers(quaryset, many=True)
        return Response(serializer.data)

class ShopDetailView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("slug",)

# class ShopDetailView(APIView):
#     # Просмотр информации о нужном магазине
#     def get(self, request, slug):
#         try:
#             shop = Shop.objects.get(slug=slug,)
#             serializer = ShopSerializers(shop)
#             return Response(serializer.data)
#         except Exception:
#             return JsonResponse({'Status': False, 'Error': 'Required page do not exist'}, status=404)


class ProductView(APIView):
    #  Создаем продукт и запрашиваем все продукты
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        quaryset = Product.objects.all()
        serializer = ProductSerializers(quaryset, many=True)
        return Response(serializer.data)


class ChangeProductView(APIView):
    # Если нужно поменять информацию о продукте
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        try:
            product = Productinfo.objects.get(id=pk)
            serializer = ProductInfoSerializers(product)
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'Status': False, 'Error': 'Requested page do not exist'},
                                status=404)

    def post(self, request, pk):
        if request.user.is_authenticated:
            user_id = request.user.id
            product = Productinfo.objects.filter(Q(id=pk) & Q(shop__shop_manager_id=user_id)).first()
            if product.exists():
                serializer = ProductInfoSerializers(product, data=request.data,
                                                    partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(serializer.errors)
            else:
                return JsonResponse({'Status': False, 'Errors': 'У вас нет прав для внесения изменений'})
        else:
            return JsonResponse({'Status': False, 'Errors': 'Нужна регистрация пользователя'})


class ProductDetailView(APIView):
    # получение списка продуктов, добавление нового.
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        quaryset = Productinfo.objects.all()
        serializer = ProductInfoSerializers(quaryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ProductInfoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class OrderView(APIView):
    # просмотр заказа, его создание (карзину условно принимать в сессии)

    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        quaryset = Order.objects.filter(user=request.user.id)
        serializer = OrderSerializers(quaryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        order = Order.objects.get_or_create(user_id=request.user.id,
                                            state="new")
        serializer = OrderItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_order_reciver.send(sender=self.__class__, user_id=request.user.id)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def put(self,request, *args, **kwargs):
        order = Order.objects.filter(user_id=request.user.id)
        serializer = OrderItemSerializers(order, data=request.data,
                                          partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ContactView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializers

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.select_related('user').filter(user_id=user)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, contact_id=pk)
        serializer = ContactSerializers(user)
        return Response(serializer.data)

    def destroy(self, request, pk, **kwargs):
        queryset = self.get_queryset()
        contact = queryset.filter(contact_id=pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers =self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def update(self, request, pk, **kwargs):
        queryset = self.get_queryset()
        partial = True # Here I change partial to True
        instance = get_object_or_404(queryset, contact_id=pk)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class ParametrView(viewsets.ModelViewSet):
    queryset = Productinfo.objects.all()
    serializer_class = ProductInfoSerializers
    filter_backends = [DjangoFilterBackend]
    filter_fields = ("productparameter",)
