from rest_framework import viewsets, permissions
from info.models import DataScienceConsultingRequest, RoboticProcessAutomationRequest, Event, Blog
from .serializers import DataScienceConsultingRequestSerializer, RoboticProcessAutomationRequestSerializer, EventSerializer, BlogSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DataScienceConsultingRequestViewSet(viewsets.ModelViewSet):
    queryset = DataScienceConsultingRequest.objects.all()
    serializer_class = DataScienceConsultingRequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Data Science Consulting Requests.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new Data Science Consulting Request.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class RoboticProcessAutomationRequestViewSet(viewsets.ModelViewSet):
    queryset = RoboticProcessAutomationRequest.objects.all()
    serializer_class = RoboticProcessAutomationRequestSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Robotic Process Automation Requests.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create a new Robotic Process Automation Request.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Events.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create a new Event.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Blogs.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create a new Blog.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
