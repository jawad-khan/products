__author__ = 'hafizmuhammadjawadkhan'
from django.contrib.auth.models import User
from django import forms

from models import profile, product, User_Product, address


class user_form(forms.ModelForm):
    class Meta:
        model = User;
        fields = ('username', 'email', 'password');
        widgets = {'password': forms.PasswordInput(), };
        help_texts = {'username': '', }


class profile_form(forms.ModelForm):
    class Meta:
        model = profile;
        fields = ('phone',);


class User_Product_form(forms.ModelForm):
    class Meta:
        model = User_Product;
        fields = ('user', 'product')


class product_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(product_form, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = ""

    class Meta:
        model = product;
        fields = '__all__'


class address_form(forms.ModelForm):
    class Meta:
        model = address;
        fields = '__all__'