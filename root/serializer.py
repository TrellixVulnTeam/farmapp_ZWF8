from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions, serializers
from .models import *

from django.contrib.auth.models import User

class FarmerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farmer_Details
        readonly_fields = ('url', 'image')

class OfficerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Officer_Details
        readonly_fields = ('url', 'image')

class CropSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop

class CropTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop_Type

class ServiceProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service_Provider

class FarmLandDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm_Land_Details
        readonly_fields = ('url', 'image')

class FarmingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farming_Type

class TransactionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction_Type

class FarmingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farming

class CropLifeCycleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop_Life_Cycle
        readonly_fields = ('url', 'image')

class YieldSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yield
        readonly_fields = ('url', 'image')

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
