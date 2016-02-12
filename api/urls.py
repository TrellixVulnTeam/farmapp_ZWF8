from django.conf.urls import url
from django.conf.urls import include

from . import views

urlpatterns = [
	url('^', include('django.contrib.auth.urls')),
	url(r'^viewmap/$',views.load_map),
]