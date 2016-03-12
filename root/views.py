from django.shortcuts import render

# Create your views here.
import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from rest_framework import exceptions, filters, generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializer import *


class NonDestructiveModelViewSet(viewsets.ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("Delete")

class OfficerViewSet(NonDestructiveModelViewSet):

    """
    Endpoint: /api/quotes/

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

        # unmapped = self.request.QUERY_PARAMS.get('unmapped')
        # include_mapped = False if unmapped == 'true' else True
        # if include_mapped or self.action == 'detail':
        #     return queryset

        # mapped_quotes = KPICampaignMinor.objects.exclude(
        #     status__in=['CNC', 'REJ', 'DEL']
        # ).values_list('quote', flat=True)

        # # Handle weird error thrown as a result of None included in list
        # mapped_quotes = [i for i in mapped_quotes if i != None]
        # queryset = queryset.exclude(id__in=mapped_quotes)
        return queryset


class farmerViewSet(NonDestructiveModelViewSet):

    """
    Endpoint: /api/quotes/

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

        # unmapped = self.request.QUERY_PARAMS.get('unmapped')
        # include_mapped = False if unmapped == 'true' else True
        # if include_mapped or self.action == 'detail':
        #     return queryset

        # mapped_quotes = KPICampaignMinor.objects.exclude(
        #     status__in=['CNC', 'REJ', 'DEL']
        # ).values_list('quote', flat=True)

        # # Handle weird error thrown as a result of None included in list
        # mapped_quotes = [i for i in mapped_quotes if i != None]
        # queryset = queryset.exclude(id__in=mapped_quotes)
        return queryset

@csrf_exempt
@api_view(['GET', 'POST', ])
def get_meta(request):
    resp = { 'farms':
    [
      {
        "farming_id": 1,
        "start_date": "2-6-2016",
        "expected_end_date": "2-8-2016",
        "no_of_units_left_for_fund": 10,
        "farming_type": "organic",
        "crop_type": "Sonamasuri",
        "crop": "rice",
        "estimated_weight_per_unit":"20kg",
        "land_details": {
            "total_area": '2',
            "area_unit": 'hector',
            "village": "ramapuram",
            "taluk": "thari",
            "district": "Nizamabad",
            "state": "Telangana",
            "latitude": 22.0006,
            "longitude":27.00007,
            "address": "near post office",
            "details": "Good yield, organic farm"
         },
         "farmer_details":{
            "name": "Narsaiah",
            "full_name": "Bugga Narsaiah",
            "address": "1-6-09/a,near post office",
            "mobile": "234988734",
            "history": "good farmer had been working hard to make living"
          },
          "officer_incharge":{
            "name": "suresh",
            "full_name": "suresh ramesh",
            "mobile": "89274923",
            "email": "sureshramesh@gmail.com",
            "qualification": "B.Sc Agriculture, 5 years of exp in farming "
            }
        },
        {
        "farming_id": 2,
        "start_date": "2-6-2016",
        "expected_end_date": "22-8-2016",
        "no_of_units_left_for_fund": 20,
        "farming_type": "organic",
        "crop_type": "Sonamasuri",
        "crop": "rice",
        "estimated_weight_per_unit":"20kg",
        "land_details": {
            "total_area": '2',
            "area_unit": 'hector',
            "village": "ramapuram",
            "taluk": "thari",
            "district": "Nizamabad",
            "state": "Telangana",
            "latitude": 23.0006,
            "longitude":26.00007,
            "address": "near post office",
            "details": "Good yield, organic farm"
         },
         "farmer_details":{
            "name": "Roshiah",
            "full_name": "Bugga Roshiah",
            "address": "1-6-09/a,near post office",
            "mobile": "234988734",
            "history": "good farmer had been working hard to make living"
          },
          "officer_incharge":{
            "name": "suresh",
            "full_name": "suresh ramesh",
            "mobile": "89274923",
            "email": "sureshramesh@gmail.com",
            "qualification": "B.Sc Agriculture, 5 years of exp in farming "
          }
        }
      ]
    }
    return HttpResponse(json.dumps(resp), content_type='application/json')


class StateViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ('name',)

class DistrictViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('state__name',)
    search_fields = ('name', )

class TalukViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Taluk.objects.all()
    serializer_class = TalukSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('state__name','district__name')
    search_fields = ('name',)

class VillageViewSet(NonDestructiveModelViewSet):

    queryset = Village.objects.all()
    serializer_class = VillageSerializer
    filter_backends = (filters.DjangoFilterBackend,filters.SearchFilter,)
    filter_fields = ('state__name','district__name','taluk__name')
    search_fields = ('name',)

