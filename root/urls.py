from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^getmeta/$', views.get_meta,name='meta' ),
]