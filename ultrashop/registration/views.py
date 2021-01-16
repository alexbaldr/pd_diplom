from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from registration.models import User
from registration.serializers import *
# from registration.tasks import send_token_task
from registration.signals import new_user_registered
# from rest_framework.renderers import TemplateHTMLRenderer


class RegisterView(APIView):
    permission_classes = [AllowAny]
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'admin.html'

    def post(self, request, *args, **kwargs):
        serializer = RegUserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            obj_user = User.objects.get(id=user.id)
            new_user_registered.send(sender=self.__class__, user_id=obj_user)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


class EnterView(APIView):
    # Вход
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'admin.html'

    def post(self, request, *args, **kwargs):
        serializer = EnterSerializers(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, email=request.data['email'],
                                password=request.data['password'])
            if user is not None:
                token = Token.objects.get_or_create(user=user)
                return JsonResponse({'Status': True, 'Token': token.key})
            # return Response(serializer.data, status.HTTP_200_OK)
        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class GetUserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer = UserSerializers

    # получение пользoвательских данных
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            quaryset = User.objects.get(id=request.user.id)
            s = self.serializer(quaryset)
            return Response(s.data)
        else:
            return JsonResponse({'Status': False, 'Errors': 'Нужна регистрация пользователя'}) 
        # редактирование пользовательских данных

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            serialiser = UserSerializers(user, data=request.data, partial=True)
            if serialiser.is_valid():
                serialiser.save()
                return Response(serialiser.data)
            else:
                return Response(serialiser.errors)
        else:
            return JsonResponse({'Status': False, 'Errors': 'Нужна регистрация пользователя'})
