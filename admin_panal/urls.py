from django.contrib import admin
from django.urls import path, include
from . import views



app_name = 'admin_panal'

urlpatterns = [
    path('add_student/', views.add_student , name='add_student'),
    path('view_students/', views.view_students, name='view_students'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    
]