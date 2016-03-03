from django.conf.urls import include, url
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'officer', views.OfficerViewSet)
router.register(r'farmer', views.farmerViewSet)

urlpatterns = [
	url(r'^getmeta/$', views.get_meta,name='meta' ),
	url(r'^', include(router.urls)),
]