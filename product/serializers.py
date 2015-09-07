from rest_framework import serializers
from django.contrib.auth.models import User
from django.conf import settings
from models import address, product, profile, user_product


class product_serializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('id', 'name', 'detail', 'price')


class address_serializer(serializers.ModelSerializer):
    class Meta:
        model = address
        fields = ('address', 'user')


class profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ('phone',)


class user_product_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_product
        fields = ('user', 'product')


class image_serializer(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields=('image',)

class user_serializer(serializers.ModelSerializer):
    phone = profile_serializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone')

    def create(self, validated_data):
        local_phone = validated_data.pop('phone')
        user = User.objects.create_user(**validated_data)
        profile.objects.create(user=user, phone=local_phone['phone'])
        return user

class complete_profile(serializers.ModelSerializer):
    user=user_serializer()

    class Meta:
        model=profile
        fields=( 'user', 'image', 'phone')
