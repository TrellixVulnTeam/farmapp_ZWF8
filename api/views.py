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
from rest_framework import exceptions, filters
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import detail_route, parser_classes
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
# Create your views here.
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from .models import *
from .permissions import IsStaffOrTargetUser, IsAdminOrIsSelf

@csrf_exempt
def load_map(request):
    return render(request, 'api/Map-search.html')

@csrf_exempt
def map_details(request):
    return render(request, 'api/Map-Details.html')

@csrf_exempt
def load_register(request):
    return render(request, 'api/Registration.html')
@csrf_exempt
def load_userdetails(request):
    return render(request, 'api/UserDetails.html')
@csrf_exempt
def load_pfdetails(request):
    return render(request, 'api/ProfileDetails.html')
@csrf_exempt
def load_tdetails(request):
    return render(request, 'api/Test.html')

class UserDetailsViewSet(RetrieveModelMixin, UpdateModelMixin, viewsets.GenericViewSet):

    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAdminOrIsSelf, IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @detail_route(methods=['POST'], permission_classes=[IsAdminOrIsSelf])
    @parser_classes((FormParser, MultiPartParser,))
    def image(self, request, *args, **kwargs):
        if 'upload' in request.data:
            user_profile = self.get_object()
            user_profile.image.delete()

            upload = request.data['upload']

            user_profile.image.save(upload.name, upload)

            return Response(status=HTTP_201_CREATED, headers={'Location': user_profile.image.url})
        else:
            return Response(status=HTTP_400_BAD_REQUEST)

class UserProfileMultiPartParserViewSet(RetrieveModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAdminOrIsSelf, IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @parser_classes((MultiPartParser,))
    def update(self, request, *args, **kwargs):
        if 'upload' in request.data:
            user_profile = self.get_object()

            user_profile.image.delete()

            upload = request.data['upload']

            user_profile.image.save(upload.name, upload)

        return super(UserProfileMultiPartParserViewSet, self).update(request, *args, **kwargs)

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    model = User
    queryset = get_user_model().objects
    # serializer_class = UserSerializer

    def get_permissions(self):
        # return (AllowAny() if self.request.method == 'POST'
        #         else IsStaffOrTargetUser()),
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserView, self).get_permissions()
