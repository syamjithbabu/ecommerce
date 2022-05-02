import email
from django.db import models

# Create your models here.
class Customer(models.Model): #inherit from Model class

    cust_id = models.AutoField(primary_key=True) #setting customer id as primary key
    cust_name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "customer"

class Seller(models.Model):
    
    seller_id = models.AutoField(primary_key=True)
    seller_name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=50)
    acc_holedr = models.CharField(max_length=30)
    acc_no = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    class Meta:
        db_table = 'seller'

