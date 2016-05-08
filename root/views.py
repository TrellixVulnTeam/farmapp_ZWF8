from django.shortcuts import render

# Create your views here.
import json
import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import Q
from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext

import cgi
from rest_framework.response import Response
from rest_framework import exceptions, filters, generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializer import *
from farmapp.settings import FILE_PATH as path


class NonDestructiveModelViewSet(viewsets.ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("Delete")

def file_upload(path, name, upload_name):
    form_data = cgi.FieldStorage()
    file_data = form_data[name].value
    fp = open(upload_name,'wb')
    fp.write(file_data)
    fp.close()

class OfficerViewSet(NonDestructiveModelViewSet):

    """
    Endpoint: /root/officer/

    GET: Typical RESTful Response including Pagination.

    `search` query parameter => ?search=<search text>

    PUT & PATCH are available though no validations
                beyond data types exist on it for now.

    """
    queryset = Officer_Details.objects.all()
    serializer_class = OfficerSerializer
    filter_backends = (filters.SearchFilter,
                       filters.DjangoFilterBackend, filters.OrderingFilter,)
    search_fields = ('name',)
    filter_fields = ('name',)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
            Default:  Send All.
            unmapped = true => Send filtered.
        """
        queryset = super().get_queryset()
        return queryset

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        status = 'Success'
        try:
            off_detail = Officer_Details.objects.create(**request.data)
            file_name = "%s-%s" % (off_detail.get('id'),off_detail.get('name'))
            file_upload(request, 'image', os.path.join(path, file_name))
            off_detail['image'] = file_name
            off_detail.save()
        except Exception as e:
            status = 'Error'

        return Response({
            'status': status})

class FarmLandDetailsViewSet(NonDestructiveModelViewSet):

    """
    Endpoint: /root/farmland/

    GET: Typical RESTful Response including Pagination.

    `search` query parameter => ?search=<search text>

    PUT & PATCH are available though no validations
                beyond data types exist on it for now.

    """
    queryset = Farm_Land_Details.objects.all()
    serializer_class = FarmLandDetailsSerializer
    filter_backends = (filters.SearchFilter,
                       filters.DjangoFilterBackend, filters.OrderingFilter,)
    search_fields = ('village__name',)
    filter_fields = ('village__name',)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
            Default:  Send All.
            unmapped = true => Send filtered.
        """
        queryset = super().get_queryset()

        return queryset

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        status = 'Success'
        try:
            off_detail = Officer_Details.objects.create(**request.data)
            file_name = "%s-%s" % (off_detail.get('id'),off_detail.get('name'))
            file_upload(request, 'image', os.path.join(path, file_name))
            off_detail['image'] = file_name
            off_detail.save()
        except Exception as e:
            status = 'Error'

        return Response({
            'status': status})

class FarmingViewSet(NonDestructiveModelViewSet):

    """
    Endpoint: /root/farming/

    GET: Typical RESTful Response including Pagination.

    `search` query parameter => ?search=<search text>

    PUT & PATCH are available though no validations
                beyond data types exist on it for now.

    """
    queryset = Farming.objects.all()
    serializer_class = FarmingSerializer
    filter_backends = (filters.SearchFilter,
                       filters.DjangoFilterBackend, filters.OrderingFilter,)
    search_fields = ('farmer_id__name',)
    filter_fields = ('farmer_id__name',)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
            Default:  Send All.
            unmapped = true => Send filtered.
        """
        queryset = super().get_queryset()

        return queryset

class CropLifeCycleViewSet(NonDestructiveModelViewSet):

    """
    Endpoint: /root/croplife/

    GET: Typical RESTful Response including Pagination.

    `search` query parameter => ?search=<search text>

    PUT & PATCH are available though no validations
                beyond data types exist on it for now.

    """
    queryset = Crop_Life_Cycle.objects.all()
    serializer_class = CropLifeCycleSerializer
    filter_backends = (filters.SearchFilter,
                       filters.DjangoFilterBackend, filters.OrderingFilter,)
    search_fields = ('farm__id',)
    filter_fields = ('farm__id',)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
            Default:  Send All.
            unmapped = true => Send filtered.
        """
        queryset = super().get_queryset()
        return queryset

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        status = 'Success'
        try:
            off_detail = Officer_Details.objects.create(**request.data)
            file_name = "%s-%s" % (off_detail.get('id'),off_detail.get('name'))
            file_upload(request, 'image', os.path.join(path, file_name))
            off_detail['image'] = file_name
            file_upload(request, 'video', os.path.join(path, file_name))
            off_detail['video'] = file_name
            off_detail.save()
        except Exception as e:
            status = 'Error'

        return Response({
            'status': status})

class YieldViewSet(NonDestructiveModelViewSet):

    """
    Endpoint: /root/yield/

    GET: Typical RESTful Response including Pagination.

    `search` query parameter => ?search=<search text>

    PUT & PATCH are available though no validations
                beyond data types exist on it for now.

    """
    queryset = Yield.objects.all()
    serializer_class = YieldSerializer
    filter_backends = (filters.SearchFilter,
                       filters.DjangoFilterBackend, filters.OrderingFilter,)
    search_fields = ('farm__id',)
    filter_fields = ('farm__id',)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
            Default:  Send All.
            unmapped = true => Send filtered.
        """
        queryset = super().get_queryset()

        return queryset

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        status = 'Success'
        try:
            off_detail = Officer_Details.objects.create(**request.data)
            file_name = "%s-%s" % (off_detail.get('id'),off_detail.get('name'))
            file_upload(request, 'image', os.path.join(path, file_name))
            off_detail['image'] = file_name
            file_upload(request, 'video', os.path.join(path, file_name))
            off_detail['video'] = file_name
            off_detail.save()
        except Exception as e:
            status = 'Error'

        return Response({
            'status': status})


class FarmerViewSet(NonDestructiveModelViewSet):

    """
    Endpoint: /root/farmer/

    GET: Typical RESTful Response including Pagination.

    `search` query parameter => ?search=<search text>

    PUT & PATCH are available though no validations
                beyond data types exist on it for now.

    """
    queryset = Farmer_Details.objects.all()
    serializer_class = FarmerSerializer
    filter_backends = (filters.SearchFilter,
                       filters.DjangoFilterBackend, filters.OrderingFilter,)
    search_fields = ('name',)
    filter_fields = ('name',)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
            Default:  Send All.
            unmapped = true => Send filtered.
        """
        queryset = super().get_queryset()
        return queryset

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        status = 'Success'
        try:
            off_detail = Officer_Details.objects.create(**request.data)
            file_name = "%s-%s" % (off_detail.get('id'),off_detail.get('name'))
            file_upload(request, 'image', os.path.join(path, file_name))
            off_detail['image'] = file_name
            off_detail.save()
        except Exception as e:
            status = 'Error'

        return Response({
            'status': status})

# @login_required
# @csrf_exempt
# @api_view(['GET', 'POST', ])
# def get_meta(request):
#     resp = { 'farms':
#     [
#       {
#         "farming_id": 1,
#         "start_date": "2-6-2016",
#         "expected_end_date": "2-8-2016",
#         "no_of_units_left_for_fund": 10,
#         "farming_type": "organic",
#         "crop_type": "Sonamasuri",
#         "crop": "rice",
#         "estimated_weight_per_unit":"20kg",
#         "land_details": {
#             "total_area": '2',
#             "area_unit": 'hector',
#             "village": "ramapuram",
#             "taluk": "thari",
#             "district": "Nizamabad",
#             "state": "Telangana",
#             "latitude": 22.0006,
#             "longitude":27.00007,
#             "address": "near post office",
#             "details": "Good yield, organic farm"
#          },
#          "farmer_details":{
#             "name": "Narsaiah",
#             "full_name": "Bugga Narsaiah",
#             "address": "1-6-09/a,near post office",
#             "mobile": "234988734",
#             "history": "good farmer had been working hard to make living"
#           },
#           "officer_incharge":{
#             "name": "suresh",
#             "full_name": "suresh ramesh",
#             "mobile": "89274923",
#             "email": "sureshramesh@gmail.com",
#             "qualification": "B.Sc Agriculture, 5 years of exp in farming "
#             }
#         },
#         {
#         "farming_id": 2,
#         "start_date": "2-6-2016",
#         "expected_end_date": "22-8-2016",
#         "no_of_units_left_for_fund": 20,
#         "farming_type": "organic",
#         "crop_type": "Sonamasuri",
#         "crop": "rice",
#         "estimated_weight_per_unit":"20kg",
#         "land_details": {
#             "total_area": '2',
#             "area_unit": 'hector',
#             "village": "ramapuram",
#             "taluk": "thari",
#             "district": "Nizamabad",
#             "state": "Telangana",
#             "latitude": 23.0006,
#             "longitude":26.00007,
#             "address": "near post office",
#             "details": "Good yield, organic farm"
#          },
#          "farmer_details":{
#             "name": "Roshiah",
#             "full_name": "Bugga Roshiah",
#             "address": "1-6-09/a,near post office",
#             "mobile": "234988734",
#             "history": "good farmer had been working hard to make living"
#           },
#           "officer_incharge":{
#             "name": "suresh",
#             "full_name": "suresh ramesh",
#             "mobile": "89274923",
#             "email": "sureshramesh@gmail.com",
#             "qualification": "B.Sc Agriculture, 5 years of exp in farming "
#           }
#         }
#       ]
#     }
#     return HttpResponse(json.dumps(resp), content_type='application/json')

@login_required
@csrf_exempt
@api_view(['GET', 'POST', ])
def get_meta(request):
    result = []
    state = request.GET.get('state')
    latitude = request.GET.get('lat')
    longitude = request.GET.get('lon')
    farm_objs = []
    if state:
        state_obj = State.objects.get(name=state)
        farm_objs = Farming.objects.filter(land__state=state_obj).select_related('land',
                                                'land__state', 'crop_type',
                                                'crop_type__crop', 'farmer',
                                                'farming_type', 'officer')
    elif latitude and longitude:
        farm_objs = Farming.objects.filter(Q(land__latitude__rangee=(latitude+2,
            latitude-2))&Q(land__longitude__rangee=(longitude+2,
            longitude-2))).select_related('land', 'land__state',
                                        'land__village', 'crop_type',
                                        'land__district', 'land__taluk',
                                        'crop_type__crop', 'farmer',
                                        'farming_type', 'officer')
    else:
        farm_objs = Farming.objects.all().select_related('land',
                                                'land__state', 'crop_type',
                                                'crop_type__crop', 'farmer',
                                                'farming_type', 'officer')
    if farm_objs:
        for obj in farm_objs:
            farm_dict = {}
            farm_dict["farming_id"] = obj.id
            farm_dict["start_date"] = obj.start_date
            farm_dict["expected_end_date"] = obj.expected_end_date
            farm_dict["no_of_units_left_for_fund"] = obj.no_of_units_for_fund
            farm_dict["crop_type"] = obj.crop_type.type_name
            farm_dict["farming_type"] = obj.farming_type.types
            farm_dict["crop"] = obj.crop_type.crop.crop_name
            farm_dict["estimated_weight_per_unit"] = str(obj.estimated_yield)
            land_details = {
                "total_area": obj.land.total_area,
                "area_unit": 'hector',
                "village": obj.land.village.name,
                "taluk": obj.land.taluk.name,
                "district": obj.land.district.name,
                "state": obj.land.state.name,
                "latitude": obj.land.latitude,
                "longitude":obj.land.longitude,
                "address": obj.land.address,
                "details": "%s, %s"%("Good yield", obj.farming_type.types)
            }
            farm_dict["land_details"] = land_details
            farmer_details = {
                "name": obj.farmer.name,
                "full_name": obj.farmer.full_name,
                "address": obj.farmer.address,
                "mobile": obj.farmer.mobile,
                "history": obj.farmer.detailed_history
            }
            farm_dict["farmer_details"] = farmer_details
            officer_incharge = {
                "name": obj.officer.name,
                "full_name": obj.officer.full_name,
                "mobile": obj.officer.mobile,
                "email": obj.officer.email,
                "qualification": obj.officer.qualification_details
            }
            farm_dict["officer_incharge"] = officer_incharge
        result.append(farm_dict)
    return Response({
            'result': result})

class CropViewSet(NonDestructiveModelViewSet):

    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ('crop_name',)

class CropTypeViewSet(NonDestructiveModelViewSet):

    queryset = Crop_Type.objects.all()
    serializer_class = CropTypeSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ('type_name',)

class ServiceProviderViewSet(NonDestructiveModelViewSet):

    queryset = Service_Provider.objects.all()
    serializer_class = ServiceProviderSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ('company_name',)

class FarmingTypeViewSet(NonDestructiveModelViewSet):

    queryset = Farming_Type.objects.all()
    serializer_class = FarmingTypeSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ('types',)

class TransactionTypeViewSet(NonDestructiveModelViewSet):

    queryset = Transaction_Type.objects.all()
    serializer_class = TransactionTypeSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ('types',)

class StateViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ('name',)

class DistrictViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('state__name','state__id')
    search_fields = ('name', )

class TalukViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Taluk.objects.all()
    serializer_class = TalukSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('state__name','district__name', 'state__id','district__id')
    search_fields = ('name',)

class VillageViewSet(NonDestructiveModelViewSet):

    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('state__name','district__name','taluk__name',
                    'state__id','district__id','taluk__id')
    search_fields = ('name',)

