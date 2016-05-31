from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, serializers
from .models import *

from django.contrib.auth.models import User

class SeedTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seed_Transaction