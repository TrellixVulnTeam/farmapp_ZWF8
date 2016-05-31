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
import datetime

import cgi
from rest_framework.response import Response
from rest_framework import exceptions, filters, generics, mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import *
from farmapp.settings import FILE_PATH as path
from django.contrib.auth.models import User
from root.models import Yield, Farming, Delivery
from api.models import *

@login_required
@csrf_exempt
@api_view(['GET', 'POST', ])
def post_fruit_data(request):
    result = []
    fruit_data = request.POST.get('fruit_fund')
    fruit_data = json.loads(fruit_data)
    order_state = fruit_data.get('order_state')
    farm_id = Farming.objects.get(id=fruit_data.get('farm_id'))
    yields = Yield.objects.get(id=fruit_data.get('trans_type'))
    try:
        fruit_obj = Fruit_Transaction(description=fruit_data.get('desc'),
                                    farm=farm_id,
                                    day=datetime.datetime.now(),
                                    user=request.user,
                                    price=fruit_data.get('amount'),
                                    no_of_units_bought=fruit_data.get('units_count'),
                                    yields=yields,
                                    order_state=order_state
                    )
        fruit_obj.save()
    except:
        return Response({
                'message': 'Failure',
                'status':'Error'})
    return Response({
            'message': 'Done',
            'status':'Success'})


def get_fruit_trans(user):
    result = []
    trans = Fruit_Transaction.objects.filter(
                            user=user).select_related(
                            'transaction_type').order_by('day')
    for tran in trans:
        trans_dict = {}
        trans_dict['id'] = tran.id
        trans_dict['transaction_type'] =  tran.transaction_type.types
        trans_dict['price'] = tran.price
        trans_dict['units'] = tran.no_of_units_bought
        trans_dict['order_state'] = tran.order_state
        result.append(trans_dict)
    return result