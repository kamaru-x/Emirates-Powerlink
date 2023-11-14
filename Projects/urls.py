from django.urls import path
from Projects import views

urlpatterns = [
    path('manage/',views.projects,name='projects'),
    path('create/',views.create_project,name='create-project'),
    path('details/<str:project_id>/',views.project_details,name='project-details'),
    path('edit/<str:project_id>/',views.edit_project,name='edit-project'),
    path('assign/pe/',views.assign_pe,name='assign-pe'),
]