from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),

    path('c-c-d/',views.c_c_d,name='c-c-d'),
    path('category/add/',views.add_category,name='add-category'),
    path('categories/',views.categories,name='categories'),
    path('category/view/<str:category_id>/',views.view_category,name='view-category'),
    path('category/edit/<str:category_id>/',views.edit_category,name='edit-category'),
    path('category/delete/',views.delete_category,name='delete-category'),

    path('sub-categories/',views.sub_categories,name='sub-categories'),
    path('sub-category/add/',views.add_sub_category,name='add-sub-category'),
    path('sub-category/edit/<str:scid>/',views.edit_sub_category,name='edit-sub-category'),
    path('sub-category/view/<str:scid>/',views.view_sub_category,name='view-sub-category'),
    path('sub-category/delete/',views.delete_sub_category,name='delete-sub-category'),

    path('sub-in-categories/',views.sub_in_categories,name='sub-in-categories'),
    path('sub-in-category/add/',views.add_sub_in_category,name='add-sub-in-category'),
    path('get-sub-categories/',views.get_sub_categories,name='get-sub-categories'),
    path('sub-in-category/edit/<str:sicid>/',views.edit_sub_in_category,name='edit-sub-in-category'),
    path('sub-in-category/view/<str:sicid>/',views.view_sub_in_category,name='view-sub-in-category'),
    path('sub-in-category/delete/',views.delete_sub_in_category,name='delete-sub-in-category'),

    path('products/',views.products,name='products'),
    path('get-sub-in-categories/',views.get_sub_in_categories,name='get-sub-in-categories'),
    path('product/add/',views.add_product,name='add-product'),
    path('product/edit/<str:product_id>/',views.edit_product,name='edit-product'),
    path('product/delete/',views.delete_product,name='delete-product'),

    path('c-u-d/',views.c_u_d,name='c-u-d'),
    path('staffs/',views.staffs,name='staffs'),
    path('staff/add/',views.add_staff,name='add-staff'),
    path('staff/details/<str:username>/',views.staff_details,name='staff-details'),
    path('staff/edit/<str:username>/',views.edit_staff,name='edit-staff'),
]