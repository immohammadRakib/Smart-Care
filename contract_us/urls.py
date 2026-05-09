from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .serializers import ContractUsSerializer
from . import views

router = DefaultRouter()
router.register('contract_us', views.ContractUsViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]