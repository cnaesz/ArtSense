from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'emotions'

urlpatterns = [
    
  path('artwork/<int:artwork_id>/submit/', views.submit_response, name='submit_response'),
]
