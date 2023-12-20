from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User


# Create your models here.
class Car(models.Model):
    image = models.ImageField(upload_to='car/media/uploads')
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12,decimal_places=3)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CarBuy(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,blank = True, null = True)
    buy_cars = models.ForeignKey(Car,on_delete=models.CASCADE,blank = True, null = True)


class Comment(models.Model):
    post = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"Comments by {self.name}"