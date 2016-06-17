from django.conf.urls import url
from django.conf.urls import include
from django.contrib.auth import views
from . import views

from django.conf.urls import patterns, url, include
from rest_framework import routers
from django.views.generic import TemplateView
 
router = routers.DefaultRouter()
router.register(r'accounts', views.UserView, 'list')
router.register(r'userdetails', views.UserDetailsViewSet)

urlpatterns = [
	url('^', include('django.contrib.auth.urls')),
	url(r'^$', TemplateView.as_view(template_name='api/index.html')),
	url(r'^register/$',views.load_register),
	url(r'^viewmap/$',views.load_map),
	url(r'^userdetails/$',views.load_userdetails),
	url(r'^profiledetails/$',views.load_pfdetails),
	url(r'^api/', include(router.urls)),
]