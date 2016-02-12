import datetime
import json
import requests

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

@csrf_exempt
def load_map(request):
    return render(request, 'api/view_map.html')