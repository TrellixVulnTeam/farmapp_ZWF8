import json
#import requests

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from django.http import *
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import *
from .permissions import IsStaffOrTargetUser

@csrf_exempt
def load_map(request):
    return render(request, 'api/Map-search.html')

@csrf_exempt
def load_register(request):
    return render(request, 'api/Registration.html')
@csrf_exempt
def load_userdetails(request):
    return render(request, 'api/UserDetails.html')
@csrf_exempt
def load_pfdetails(request):
    return render(request, 'api/ProfileDetails.html')

class UserView(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserView, self).get_permissions()