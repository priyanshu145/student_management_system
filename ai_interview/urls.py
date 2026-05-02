from django.urls import path
from . import views

app_name = 'ai_interview'

urlpatterns = [
    path('upload-resume/', views.upload_resume, name='upload_resume'),
    path('video-interview/<int:session_id>/', views.video_interview, name='video_interview'),
]