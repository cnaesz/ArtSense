from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'artworks'

urlpatterns = [
    path('showarts/', views.show_artwork, name='showarts'),
    path('',include('emotions.urls', namespace='emotions')),
]
