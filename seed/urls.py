from django.conf.urls import include, url
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'seedpost', views.SeedTransactionViewSet)

urlpatterns = [
    url(r'^post/$', views.post_seed_data,name='postseed' ),
    url(r'^', include(router.urls)),
]