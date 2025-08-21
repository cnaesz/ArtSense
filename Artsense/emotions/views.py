from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from artworks.models import Artwork
from .models import Response
# Create your views here.

def save_response(request, artwork_met_id):
    if request.method == 'POST':
        word = request.POST.get('word', '').strip()
        artwork = get_object_or_404(Artwork, met_id=artwork_met_id)
        if word:

          Response.objects.create(
              user=request.user,
              artwork=artwork,
              word=word,
              normalized_word=word.lower(),
          )
  # Or wherever you want
    return redirect('artworks:showarts')