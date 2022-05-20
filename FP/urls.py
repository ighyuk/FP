from django.urls import path

from . import views

app_name = 'FP'

urlpatterns = [
    path('detectme', views.detectme, name='detectme'),
    path('', views.index, name='index'),
    path('<int:user_id>/', views.detail, name='detail'),
    path('management', views.management, name='management'),
    path('visitRecord', views.visitRecord, name='visitRecord'),
    path('chat', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
]