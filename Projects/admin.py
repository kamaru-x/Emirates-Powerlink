from django.contrib import admin
from Projects.models import Project

# Register your models here.

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['Project_Name','Client_Name','Client_Mobile','Contact_Name','Contact_Number','Expected_Starting_Date','Expected_Amount']