from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.db.models import Sum
from django.shortcuts import reverse
type_stocks=(
    ('stock1','stock1'),
('stock2','stock2'))
class stocks(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    stock1=models.IntegerField(default=0)
    stock2=models.IntegerField(default=0)

class trade(models.Model):
    seller=models.ForeignKey(settings.AUTH_USER_MODEL,related_name='seller_of_stock',on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    stock=models.CharField(choices=type_stocks,max_length=100)
    buyer=models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='buyer_of_stock',on_delete=models.CASCADE)    
