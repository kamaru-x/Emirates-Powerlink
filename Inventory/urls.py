from django.urls import path
from Inventory import views

urlpatterns = [
    path('',views.inventory,name='inventory'),
    path('projects/',views.project_inventory,name='projects-inv'),
    path('category/add/',views.inventory_category,name='inv-cat-add'),
    path('items/in/',views.inventory_in,name='inventory-in'),
    path('items/out/',views.inventory_out,name='inventory-out'),

    path('view/<str:quotation_id>/',views.inventory_view,name='inventory-view'),
    path('add/<str:quotation_id>/',views.add_to_inventory,name='add-to-inventory'),
]