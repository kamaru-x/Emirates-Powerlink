from django.urls import path
from Quotation import views

urlpatterns = [
    path('compare/<str:reference>/',views.compare,name='compare'),
    path('receive/<str:reference>/',views.receive_quotation,name='receive-quotation'),
    path('accept/',views.accept_quotation,name='accept-quotation'),
    path('approved/',views.quotations,name='quotations'),
    path('view/<str:reference>/',views.view_quotation,name='view-quotation'),
    path('convert/<str:reference>/',views.convert_to_lpo,name='convert-to-lpo'),
    path('lpos/',views.lpos,name='lpos'),
    path('print/lpo/<str:reference>',views.print_lpo,name='print-lpo'),
    path('lpo/edit/<int:id>/',views.edit_lpo,name='edit-lpo')
]