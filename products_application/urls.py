from django.urls import path
from . import views

app_name='products_application' 

urlpatterns=[
    path('', views.get_all_products_screen, name='products_list_screen'),
    path('add/', views.add_product_screen, name='add_product_screen'),
    path('<int:id>/',views.get_single_product_detail_screen, name='product_details_screen'),
    path('<int:id>/edit',views.edit_product_screen, name='edit_product_screen'),
    path('<int:id>/delete',views.delete_product_action, name='delete_product_action'),
]

