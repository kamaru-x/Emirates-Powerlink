from django.contrib import admin
from Projects.models import Project,Expense

# Register your models here.

@admin.register(Project)
class ProjectModelAdmin(admin.ModelAdmin):
    list_display = ['Project_Name','Job_No','Client_Name','Client_Mobile','Contact_Name','Contact_Number']

@admin.register(Expense)
class ExpenseModelAdmin(admin.ModelAdmin):
    list_display = ['Title','Amount','Category','Date','Project']