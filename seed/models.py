from django.db import models
from farmapp.root.models import *
from farmapp.api import *

# Create your models here.
class Transaction(models.Model):
    description = models.TextField()
    farm = models.ForeignKey(Farming)
    day = models.DateField()
    delivery = models.ForeignKey(Delivery)
    user = models.ForeignKey(User)
    price = models.FloatField()
    no_of_units_bought = models.IntegerField()
    transaction_type = models.ForeignKey(Transaction_Type)

class Fund(models.Model):
    description = models.TextField()
    farm = models.ForeignKey(Farming)
    price = models.FloatField()
    transaction = models.ForeignKey(Transaction)

