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
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['GET', 'POST', ])
def get_meta(request):
    resp = {
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
              "mandal": "thari",
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
              "qualification": "B.Sc Agriculture, 5 years of exp in farming ",
          
            }
        }
    return HttpResponse(json.dumps(resp), content_type='application/json')