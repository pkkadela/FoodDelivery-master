from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    isVeg = models.BooleanField()
    photo = models.ImageField(default='default.jpg', upload_to='food_pics')
    price =  models.PositiveIntegerField()
    index = models.AutoField(primary_key=True)
    cart = models.ForeignKey("user.cart", on_delete=models.SET_NULL, null=True, blank=True)