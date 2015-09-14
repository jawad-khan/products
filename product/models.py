import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name="phone")
    image = models.ImageField(default='default.jpg')
    phone = models.CharField(max_length=55, null=False, blank=False)
    cover = models.ImageField(default='default_cover.jpg')


COUNTRIES = (
    ('PK', 'Pakistan'),
    ('US', 'USA'),
    ('UK', 'England'),
    ('AS', 'Australia'),
    ('NZ', 'NewZeland')
)


class Address(models.Model):
    user = models.ForeignKey(User);
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=2, choices=COUNTRIES, default='PK')


class Product(models.Model):
    name = models.CharField(max_length=15, null=False, blank=False)
    detail = models.CharField(max_length=25, )
    price = models.IntegerField(default=0, blank=False)
    image = models.ImageField(default='default_product.jpg')


class UserProduct(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product,related_name="product")
    bought_at = models.DateTimeField(default=datetime.datetime.now)
