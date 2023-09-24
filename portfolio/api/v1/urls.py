from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompetenceViewSet, EducationViewSet, ExperienceViewSet, ProjectViewSet

router = DefaultRouter()
router.register(r'competences', CompetenceViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

