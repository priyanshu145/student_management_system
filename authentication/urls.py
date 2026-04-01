from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'authentication'

urlpatterns = [
     path('teacher_login/',  views.teacher_login, name = 'teacher_login'),
     path('teacher_dash/', views.teacher_dashboard, name= 'teacher_dashboard'),
     path('student_login/' , views.student_login, name = 'student_login'),
     path('admin_login/', views.admin_login, name='admin_login'),
     path('admin_dash/', views.admin_dashboard, name='admin_dashboard'),
     path('student_dash/', views.student_dashboard, name='student_dashboard'),
]