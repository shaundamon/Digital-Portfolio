# Create urls for the api

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataScienceConsultingRequestViewSet, RoboticProcessAutomationRequestViewSet, EventViewSet, BlogViewSet

router = DefaultRouter()
router.register(r'data-science-consulting-requests', DataScienceConsultingRequestViewSet)
router.register(r'robotic-process-automation-requests', RoboticProcessAutomationRequestViewSet)
router.register(r'events', EventViewSet)
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]