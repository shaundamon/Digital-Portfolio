from django.contrib import admin
from django.urls import path, include
# from .models import MyModel
from .views import (
    homePage,
    projectsPage,
    projectDetail,
    search,
    handler404,
    blogDetail
)

from django.conf import settings
from django.conf.urls.static import static

# admin.site.register(models.models)

handler404 = handler404

urlpatterns = [

        path('', homePage, name='homePage'),
        path('projects/', projectsPage, name='projectsPage'),
        path('projects/<str:slug>/', projectDetail, name='projectDetail'),
        path('search/', search, name='search'),
        path('blog/', blogDetail, name='blogDetail'),
        path('blog/<str:slug>/', blogDetail, name='blogDetail'),

        # include the admin panel urls
        path('admin/', admin.site.urls),
        path('dashboard/', include('dashboard.urls')),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
