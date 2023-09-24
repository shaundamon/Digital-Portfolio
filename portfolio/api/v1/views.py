from rest_framework import viewsets
from info.models import Competence, Education, Experience, Project
from .serializers import CompetenceSerializer, EducationSerializer, ExperienceSerializer, ProjectSerializer

class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    http_method_names = ['get', 'post']

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    http_method_names = ['get', 'post']

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    http_method_names = ['get', 'post']

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post']
