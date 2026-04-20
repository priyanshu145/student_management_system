from django.urls import path
from . import views

app_name = 'Student'

urlpatterns = [
    path('ai-analysis/', views.ai_analysis, name='ai_analysis'),
]