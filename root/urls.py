from django.conf.urls import include, url
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'officer', views.OfficerViewSet)
router.register(r'farmer', views.FarmerViewSet)
router.register(r'farmland', views.FarmLandDetailsViewSet)
router.register(r'farming', views.FarmingViewSet)
router.register(r'lifecycle', views.CropLifeCycleViewSet)
router.register(r'yield', views.YieldViewSet)
router.register(r'crop', views.CropViewSet)
router.register(r'croptype', views.CropTypeViewSet)
router.register(r'serviceprovider', views.ServiceProviderViewSet)
router.register(r'farmtype', views.FarmingTypeViewSet)
router.register(r'transtype', views.TransactionTypeViewSet)
router.register(r'state', views.StateViewSet)
router.register(r'district', views.DistrictViewSet)
router.register(r'taluk', views.TalukViewSet)
router.register(r'village', views.VillageViewSet)

urlpatterns = [
    url(r'^getmeta/$', views.get_meta, name='meta'),
    url(r'^getrans/$', views.get_transaction, name='transaction'),
    url(r'^', include(router.urls)),
]