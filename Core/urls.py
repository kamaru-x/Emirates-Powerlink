from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),

    path('c-c-d/',views.c_c_d,name='c-c-d'),
    path('category/add/',views.add_category,name='add-category'),
    path('categories/',views.categories,name='categories'),
    path('category/edit/<str:category_id>/',views.edit_category,name='edit-category'),

    path('products/',views.products,name='products'),
    path('product/add/',views.add_product,name='add-product'),
    path('product/edit/<str:product_id>/',views.edit_product,name='edit-product'),

    path('c-u-d/',views.c_u_d,name='c-u-d'),
    path('staffs/',views.staffs,name='staffs'),
    path('staff/add/',views.add_staff,name='add-staff'),
    path('staff/details/<str:username>/',views.staff_details,name='staff-details'),
    path('staff/edit/<str:username>/',views.edit_staff,name='edit-staff'),
]