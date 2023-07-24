import queue
from django.db import models

# Create your models here.

class Order(models.Model):
    
    product = models.CharField( max_length=50)
    code = models.CharField(max_length=50)
    coupon = models.IntegerField()
    counter = models.IntegerField()
    queue = models.IntegerField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.product