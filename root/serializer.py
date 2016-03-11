from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, serializers
from .models import *

from django.contrib.auth.models import User

class FarmerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farmer_Details
        #fields = ('id', 'username')

class OfficerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Officer_Details
        #fields = ('id', 'username')

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State

class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District

class TalukSerializer(serializers.ModelSerializer):

    class Meta:
        model = Taluk

class VillageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Village
