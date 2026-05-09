from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('doctorlist', views.DoctorViewSet)
router.register('designation', views.DesignationViewSet)
router.register('special', views.SpecialViewSet)
router.register('time', views.AvailableTimeViewSet)
router.register('review', views.ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]