from django.contrib import admin
from django.urls import path, include
# from .models import MyModel
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
                        robotic_process_automation, process_optimization, events, blog, send_email, form_submission)

from django.conf import settings
from django.conf.urls.static import static

# admin.site.register(models.models)

handler404 = handler404

urlpatterns = [

    path('', homePage, name='homePage'),
    path('projects/', projectsPage, name='projectsPage'),
    path('projects/<str:slug>/', projectDetail, name='projectDetail'),
    path('search/', search, name='search'),
    path('blog/', blog, name='blog'),
    path('success/', success, name='success'),
    path('blog/<str:slug>/', blogDetail, name='blogDetail'),
    path('events/', events, name='events'),
    path('send_email/', send_email, name='send_email'),
    path('form_submission/', form_submission, name='form_submission'),
    path('data-science-consulting/', data_science_consulting,
         name='data_science_consulting'),
    path('robotic-process-automation/', robotic_process_automation,
         name='robotic_process_automation'),
    path('process-optimization/', process_optimization,
         name='process_optimization'),

    # include the admin panel urls
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
