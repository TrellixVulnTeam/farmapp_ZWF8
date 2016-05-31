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
#from root.views import NonDestructiveModelViewSet
from api.models import *



class NonDestructiveModelViewSet(viewsets.ModelViewSet):

    def destroy(self, request, *args, **kwargs):
        raise exceptions.MethodNotAllowed("Delete")

@login_required
@csrf_exempt
@api_view(['POST', ])
def post_seed_data(request):
    result = []
    seed_data = request.POST.get('seed_fund')
    seed_data = json.loads(seed_data)
    order_state = seed_data.get('order_state')
    farm_id = Farming.objects.get(id=seed_data.get('farm_id'))
    trans_type = Transaction_Type.objects.get(id=seed_data.get('trans_type'))
    try:
        seed_obj = Seed_Transaction(description=seed_data.get('desc'),
                                    farm=farm_id,
                                    day=datetime.datetime.now(),
                                    user=request.user,
                                    price=seed_data.get('amount'),
                                    no_of_units_bought=seed_data.get('units_count'),
                                    transaction_type=trans_type,
                                    order_state=order_state
                    )
        seed_obj.save()
    except Exception as e:
        return Response({
                'msg': str(e),
                'message': 'Failure',
                'status':'Error'})
    return Response({
            'message': 'Done',
            'status':'Success'})

class SeedTransactionViewSet(NonDestructiveModelViewSet):

    """
    Endpoint: /seed/post/

    GET: Typical RESTful Response including Pagination.

    `search` query parameter => ?search=<search text>

    PUT & PATCH are available though no validations
                beyond data types exist on it for now.

    """
    queryset = Seed_Transaction.objects.all()
    serializer_class = SeedTransactionSerializer
    filter_backends = (filters.SearchFilter,
                       filters.DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
            Default:  Send All.
            unmapped = true => Send filtered.
        """
        queryset = super().get_queryset()
        return queryset

def get_seed_trans(user):
    result = []
    try:
        trans = Seed_Transaction.objects.filter(
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
    except Exception as e:
        return [str(e)]
    return result


