from rest_framework import viewsets
from info.models import Competence, Education, Experience, Project
from .serializers import CompetenceSerializer, EducationSerializer, ExperienceSerializer, ProjectSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Competences.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create a new Competence.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Educations.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create a new Education.")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Experiences.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Projects.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
