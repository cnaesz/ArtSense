from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import requests
from django.contrib.auth.decorators import login_required

from .models import Artwork
import random

@login_required
def show_artwork(request):
    all_artworks = Artwork.objects.all()
    if all_artworks.exists():
        artwork = random.choice(list(all_artworks))
    else:
        artwork = None

    return render(request, 'artworks/artworks.html', {'artwork': artwork})

