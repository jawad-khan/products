import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name="phone")
    image=models.ImageField(upload_to="users",default='/products/default.jpg')
    phone = models.CharField(max_length=55, null=False, blank=False)


class address(models.Model):
    user = models.ForeignKey(User);
    address = models.CharField(max_length=50)


class product(models.Model):
    Name = models.CharField(max_length=15, null=False, blank=False);
    Detail = models.CharField(max_length=25, );
    Price = models.IntegerField(default=0, blank=False);


class User_Product(models.Model):
    user = models.ForeignKey(User);
    product = models.ForeignKey(product);
    bought_at = models.DateTimeField(default=datetime.datetime.now)
