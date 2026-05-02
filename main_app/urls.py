from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main_app'

urlpatterns = [
     path('', views.index , name = 'index'),
     path('logout/', views.logout_views, name='logout'),
     path("contact/", views.contact, name="contact"),
     path("courses/", views.courses, name="courses"),
     
    
]