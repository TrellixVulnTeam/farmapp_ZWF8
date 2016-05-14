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
from datetime

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
from django.contrib.auth.models import User
from root.models import Transaction_Type, Farming, Delivery
from api.models import *

@login_required
@csrf_exempt
@api_view(['GET', 'POST', ])
def post_seed_data(request):
    result = []
    seed_data = request.POST.get('seed_fund')
    farm_id = Farming.objects.get(id=seed_data.get('farm_id'))
    trans_type = Transaction_Type.objects.get(id=seed_data.get('trans_type'))
    try:
        seed_obj = Seed_Transaction(description=seed_data.get('desc'),
                                    farm=farm_id,
                                    day=datetime.datetime.now(),
                                    user=request.user,
                                    price=seed_data.get('amount'),
                                    no_of_units_bought=seed_data.get('units_count'),
                                    transaction_type=trans_type
                    )
        seed_obj.save()
    except:
        return Response({
                'message': 'Failure',
                'status':'Error')
    return Response({
            'message': 'Done',
            'status':'Success')
