from django.db import models
from django.contrib.auth.models import User
from root.models import *
from api.models import *

# Create your models here.
class Fruit_Transaction(models.Model):
    description = models.TextField(null=True, blank=True)
    farm = models.ForeignKey(Farming)
    day = models.DateField()
    delivery = models.ForeignKey(Delivery, null=True, blank=True)
    user = models.ForeignKey(User)
    price = models.FloatField(null=True, blank=True)
    no_of_units_sold = models.IntegerField()
    yields = models.ForeignKey(Yield, null=True, blank=True)
    states = (
        ("created", "created"),
        ("pending", "pending"),
        ("fineshed", "fineshed")
    )
    order_state = models.CharField(max_length=50, choices=states)
    external_id = models.CharField(max_length=256, null=True, blank=True)
