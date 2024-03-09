from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import (
    homePage,
    projectsPage,
    projectDetail,
    search,
    handler404,
    blogDetail,
    success,

)
from info.views import (data_science_consulting,
                        robotic_process_automation, process_optimization, 
                        events, blog, blog_list, send_email, form_submission, 
                        experiences_and_education, languages_and_tools)

from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


schema_view = get_schema_view(
    openapi.Info(
        title="Shaun's Portfolio API",
        default_version='v1',
        description="This is the API for Shaun's Portfolio. It contains all the data for the portfolio website. The API is built using Django Rest Framework and the documentation is built using swagger UI",
    ),
    public=True,
)

handler404 = handler404

urlpatterns = [

    path('', homePage, name='homePage'),
    path('projects/', projectsPage, name='projectsPage'),
    path('projects/<str:slug>/', projectDetail, name='projectDetail'),
    path('search/', search, name='search'),
    path('blog/', blog_list, name='blog_list'),
    path('success/', success, name='success'),
    path('blog/<str:slug>/', blogDetail, name='blogDetail'),
    path('events/', events, name='events'),
    path('send_email/', send_email, name='send_email'),
    path('form_submission/', form_submission, name='form_submission'),
    path('experiences_and_education/', experiences_and_education,
         name='experiences_and_education'),
    path('languages-and-tools/', languages_and_tools, name='languages_and_tools'),
    path('data-science-consulting/', data_science_consulting,
         name='data_science_consulting'),
    path('robotic-process-automation/', robotic_process_automation,
         name='robotic_process_automation'),
    path('process-optimization/', process_optimization,
         name='process_optimization'),

    # include the admin panel urls
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),

    # include the portfolio api urls
    path('api/portfolio/v1/', include('portfolio.api.v1.urls')),

    # include the info api urls
    path('api/info/v1/', include('info.api.v1.urls')),

    # Add swagger UI styles
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
