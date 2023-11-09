from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('c-c-d/',views.c_c_d,name='c-c-d'),
    path('add-category/',views.add_category,name='add-category'),
    path('categories/',views.categories,name='categories'),
    path('edit-category/<str:category_id>/',views.edit_category,name='edit-category')
]