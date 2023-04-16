from django.contrib import admin
from .models import Competence, Education, Experience, Project, Message, Information, Event, Tag

class TagAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Information)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Competence)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Message)
admin.site.register(Event)
admin.site.register(Tag, TagAdmin)
