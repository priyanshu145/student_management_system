from django.urls import path
from . import views

app_name = 'scan'

urlpatterns = [
    path('scan_upload/', views.scan_upload, name='scan_upload'),
]