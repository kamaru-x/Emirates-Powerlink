from django.urls import path
from Requisition import views

urlpatterns = [
    path('create/<str:project_id>/',views.create_requisition,name='create-requisition'),
    path('edit/<str:reference>/',views.requisition,name='requisition'),
    path('get-products/',views.get_products,name='get-products'),
    path('add/item/',views.add_requisition_item,name='add-requisition-item'),
    path('status/',views.requisitions,name='requisitions'),
    path('view/<str:reference>/',views.view_requisition,name='view-requisition'),
    path('print/<str:reference>/',views.print_requisition,name='print-requisition'),
    path('approve/<str:reference>/',views.approve_requisition,name='approve-requisition'),
    path('reject/<str:reference>/',views.reject_requisition,name='reject-requisition'),
]