from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'authentication'

urlpatterns = [
     path('student_login/' , views.student_login, name = 'student_login'),
     path('admin_login/', views.admin_login, name='admin_login'),
     path('admin_dash/', views.admin_dashboard, name='admin_dashboard'),
     path('student_dash/', views.student_dashboard, name='student_dashboard'),
]