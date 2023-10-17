from django.contrib import admin
from plugD.models import Project




class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'file_number']




admin.site.register(Project, ProjectAdmin)