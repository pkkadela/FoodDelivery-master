from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from food.models import Food

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)

class Details(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    state = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()
    postcode = models.CharField(max_length=6)
