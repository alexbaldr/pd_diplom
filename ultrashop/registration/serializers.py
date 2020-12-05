from rest_framework import serializers
from registration.models import User


class RegUserSerializers(serializers.ModelSerializer):
    # Регистрация пользователя

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email', 'password', )


class UserSerializers(serializers.ModelSerializer):
    # Отображение данных пользователя, с возможностью для изменений даннных.

    class Meta:
        model = User
        fields = "__all__" #('username', 'first_name', 'last_name', 'email',
                #   'password', 'last_login', 'is_active',
                #   'bio', 'birth_date', 'is_superuser',
                #   )


class EnterSerializers(serializers.ModelSerializer):
    # Вход пользователя
    class Meta:
        model = User
        fields = ["email", 'password', ]
