from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'teacher'

urlpatterns = [
   path("add_marks/", views.add_marks, name="add_marks")
]