from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chatroom'),
    path('<str:room_name>/', views.room, name='room'),
]
