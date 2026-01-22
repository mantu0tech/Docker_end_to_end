from django.urls import path
from my_to_do_list_app import views

urlpatterns = [
    path('', views.to_do_list_view, name='to_do_list'),
    path('to-do-list/add-page/', views.to_do_create_view, name='to_do_create'),
    path('to-do-list/update-page/<slug:slug>/', views.to_do_update_view, name='to_do_update'),
    path('to-do-list/delete-page/<slug:slug>/', views.to_do_delete_view, name='to_do_delete'),
]
