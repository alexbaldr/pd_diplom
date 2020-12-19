from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from registration.serializers import *
from registration.models import User
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework import status
from registration.signals import new_user_registered
from registration.tasks import send_token_task


class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = RegUserSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            obj_user = User.objects.get(id=user.id)
            send_token_task.delay(user_id=obj_user) # выскакивает ошибка рэдиса
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class EnterView(APIView):
    # Вход
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = EnterSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(request, email=request.data['email'],
                                password=request.data['password'])
            return Response(serializer.data, status=status.HTTP_200_OK,)

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
