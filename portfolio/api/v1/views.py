from rest_framework import viewsets
from info.models import Competence, Education, Experience, Project
from .serializers import CompetenceSerializer, EducationSerializer, ExperienceSerializer, ProjectSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



class CompetenceViewSet(viewsets.ModelViewSet):
    """
    Competence API View Set

    This API endpoint allows for the management of 'Competence' objects. It supports both GET and POST HTTP methods.
    
    HTTP Methods Supported:
    - GET: To retrieve a list of all Competence records.
    - POST: To create a new Competence record.

    Headers Accepted:
    - Content-Type: application/json
    - Authorization: Bearer <token>
    """
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Competences.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        """
        List all Competence instances.

        This method retrieves all the existing Competence records. 
        
        Optional Query Parameters:
        - some_param (String): A custom query parameter for additional filtering or sorting. For example, you can use this to filter Competence records based on a certain criteria.

        Returns:
        - A JSON object containing a list of Competence records.

        Example Request:
        GET /api/competence/?some_param=value

        Example Response:
        [
            {
                "id": 1,
                "name": "Python",
                "level": "Expert"
            },
            {
                "id": 2,
                "name": "Java",
                "level": "Intermediate"
            }
        ]
        """
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create a new Competence.")
    def create(self, request, *args, **kwargs):
        """
        Create a new Competence instance.

        This method allows you to create a new Competence record. You need to provide all the required fields in the request body.

        Request Body:
        - name (String): The name of the competence. For example, "Python".
        - level (String): The level of competence. For example, "Expert".

        Returns:
        - A JSON object representing the newly created Competence record.

        Example Request:
        POST /api/competence/
        {
            "name": "JavaScript",
            "level": "Beginner"
        }

        Example Response:
        {
            "id": 3,
            "name": "JavaScript",
            "level": "Beginner"
        }
        """
        return super().create(request, *args, **kwargs)

class EducationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for handling Education objects.
    Supports: GET, POST
    """
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Educations.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        """
        List all Education instances.
        Supports optional query parameters:
            some_param: Description
        """
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(operation_description="Create a new Education.")
    def create(self, request, *args, **kwargs):
        """
        Create a new Education instance.
        """
        return super().create(request, *args, **kwargs)

class ExperienceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for handling Experience objects.
    Supports: GET, POST
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Experiences.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        """
        List all Experience instances.
        Supports optional query parameters:
            some_param: Description
        """
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        """
        Create a new Experience instance.
        """
        return super().create(request, *args, **kwargs)
    

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint for handling Project objects.
    Supports: GET, POST
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve a list of all Projects.", manual_parameters=[openapi.Parameter('some_param', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)])
    def list(self, request, *args, **kwargs):
        """
        List all Project instances.
        Supports optional query parameters:
            some_param: Description
        """
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        """
        Create a new Project instance.
        """
        return super().create(request, *args, **kwargs)
