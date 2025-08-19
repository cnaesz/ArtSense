from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('showimg/', views.show_artwork, name='showimage'),

]
