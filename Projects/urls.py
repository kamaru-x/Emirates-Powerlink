from django.urls import path
from Projects import views

urlpatterns = [
    path('manage/',views.projects,name='projects')
]