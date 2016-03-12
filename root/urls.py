from django.conf.urls import include, url
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'officer', views.OfficerViewSet)
router.register(r'farmer', views.farmerViewSet)
router.register(r'state', views.StateViewSet)
router.register(r'district', views.DistrictViewSet)
router.register(r'taluk', views.TalukViewSet)
router.register(r'village', views.VillageViewSet)

urlpatterns = [
	url(r'^getmeta/$', views.get_meta,name='meta' ),
	url(r'^', include(router.urls)),
]