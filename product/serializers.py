from rest_framework import serializers
from django.contrib.auth.models import User

from models import Address, Product, Profile, UserProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'detail', 'price', 'image')


class AddressSerializer(serializers.ModelSerializer):
    country = serializers.SerializerMethodField()
    class Meta:
        model = Address
        fields = ('address', 'user', 'country')
    def get_country(self,obj):
        return obj.get_country_display()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone',)


class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = ('user', 'product')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('image',)


class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('cover',)


class UserSerializer(serializers.ModelSerializer):
    phone = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone')

    def create(self, validated_data):
        local_phone = validated_data.pop('phone')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, phone=local_phone['phone'])
        return user


class CompleteProfile(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ( 'user', 'image', 'phone', 'cover')
