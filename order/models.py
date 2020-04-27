from django.db import models
from product.models import Products
from maincsi.utils import unique_order_id_genrator
from django.db.models.signals import pre_save,post_save

# Create your models here.


class Order_all(models.Model):
    order_id =models.CharField(max_length=50,blank=True,null=True)
    product  =models.ForeignKey(Products,on_delete=models.CASCADE)
    total    =models.IntegerField(blank=True,null=True)
    Name     =models.CharField(max_length=100,blank=True,null=True)
    Email     =models.EmailField(max_length=100,blank=True,null=True)
    Contact  =models.IntegerField(blank=True,null=True)
    Address1 =models.CharField(max_length=120)
    Address2 =models.CharField(max_length=120,blank=True,null=True)
    City     =models.CharField(max_length=25)
    State    =models.CharField(max_length=25)
    Pincode  =models.IntegerField()

    def __str__(self):
        return str(self.order_id)

    def update_total(self):
        prod_total=self.product.real_price
        self.total=prod_total
        self.save()
        return prod_total



def pre_save_total(sender,created,instance,*args,**kwargs):
    if created:
        instance.update_total()

post_save.connect(pre_save_total,sender=Order_all)


def pre_save_order_id(sender,instance,*args, **kwargs):
    if not  instance.order_id:
        instance.order_id=unique_order_id_genrator(instance)
pre_save.connect(pre_save_order_id,sender=Order_all)