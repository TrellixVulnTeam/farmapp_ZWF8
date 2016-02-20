from django.db import models
from django.contrib.auth.models import User
from root.models import *
from api.models import *

# Create your models here.
class Seed_Transaction(models.Model):
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
    transaction = models.ForeignKey(Seed_Transaction)

