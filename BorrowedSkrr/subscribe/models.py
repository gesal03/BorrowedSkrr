from django.db import models
from accounts.models import Empolyee

# Create your models here.
class Product(models.Model):
    CATEGROY_CHOICES = (
        ("1", "Laptop/SmartGear"),
        ("2", "Sound"),
        ("3", "Camera"),
        ("4", "Game/VR")
    )

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    count = models.PositiveIntegerField(default=0)
    priceWeek = models.PositiveIntegerField(default=0)
    priceMonth = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    categroy = models.CharField(max_length=30, choices=CATEGROY_CHOICES, default="1")

    def __str__(self):
        return self.name


class EmpolyeeWishList(models.Model):
    empolyee_id = models.ForeignKey(Empolyee, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.empolyee_id.name
    
class Shopping(models.Model):
    empolyee_id = models.ForeignKey(Empolyee, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    startDate = models.DateField(auto_now_add=True)
    endDate = models.DateField()
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.empolyee_id.name

class Subscribe(models.Model):
    empolyee_id = models.ForeignKey(Empolyee, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)
    startDate = models.DateField(auto_now_add=True)
    endDate = models.DateField()
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.empolyee_id.name