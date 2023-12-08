from django.urls import path
from Requisition import views

urlpatterns = [
    path('create/<str:project_id>/',views.create_requisition,name='create-requisition'),
    path('edit/<str:reference>/',views.requisition,name='requisition'),
    path('get-products/',views.get_products,name='get-products'),
    path('add/item/',views.add_requisition_item,name='add-requisition-item'),
    path('add/new/item/',views.add_new_item,name='add-new-item'),
    path('add/service/<str:requisition_id>/',views.service_requisition,name='service-requisition'),
    path('delete/attachment/<str:attachment_id>/',views.delete_attachment,name='delete_attachment'),
    path('delete/item/',views.delete_requisition_item,name='delete-requisition-item'),
    path('status/',views.requisitions,name='requisitions'),
    path('view/<str:reference>/',views.view_requisition,name='view-requisition'),
    path('print/<str:reference>/',views.print_requisition,name='print-requisition'),
    path('approve/<str:reference>/',views.approve_requisition,name='approve-requisition'),
    path('reject/<str:reference>/',views.reject_requisition,name='reject-requisition'),
    path('check/<str:reference>/',views.check_requisition,name='check-requisition'),
]