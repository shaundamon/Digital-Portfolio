from rest_framework import viewsets, permissions
from info.models import DataScienceConsultingRequest, RoboticProcessAutomationRequest, Event, Blog
from .serializers import DataScienceConsultingRequestSerializer, RoboticProcessAutomationRequestSerializer, EventSerializer, BlogSerializer

class DataScienceConsultingRequestViewSet(viewsets.ModelViewSet):
    queryset = DataScienceConsultingRequest.objects.all()
    serializer_class = DataScienceConsultingRequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

class RoboticProcessAutomationRequestViewSet(viewsets.ModelViewSet):
    queryset = RoboticProcessAutomationRequest.objects.all()
    serializer_class = RoboticProcessAutomationRequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']
