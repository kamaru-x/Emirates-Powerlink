from django.urls import path
from Inventory import views

urlpatterns = [
    path('projects/',views.project_inventory,name='project-inventory'),
    path('view/<str:quotation_id>/',views.inventory_view,name='inventory-view'),
    path('add/<str:quotation_id>/',views.add_to_inventory,name='add-to-inventory'),
]