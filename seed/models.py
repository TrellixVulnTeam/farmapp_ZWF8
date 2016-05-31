from django.db import models
from django.contrib.auth.models import User
from root.models import Farming, Delivery, Transaction_Type
from api.models import *

# Create your models here.
class Seed_Transaction(models.Model):
    description = models.TextField(null=True, blank=True)
    farm = models.ForeignKey(Farming)
    day = models.DateField()
    delivery = models.ForeignKey(Delivery, null=True, blank=True)
    user = models.ForeignKey(User)
    price = models.FloatField(null=True, blank=True)
    no_of_units_bought = models.IntegerField()
    transaction_type = models.ForeignKey(Transaction_Type)
    states = (
        ("created", "created"),
        ("pending", "pending"),
        ("fineshed", "fineshed")
    )
    order_state = models.CharField(max_length=50, choices=states)
    external_id = models.CharField(max_length=256, null=True, blank=True)

class Fund(models.Model):
    description = models.TextField()
    farm = models.ForeignKey(Farming)
    price = models.FloatField()
    transaction = models.ForeignKey(Seed_Transaction)

