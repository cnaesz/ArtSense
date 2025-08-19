
from django.db import models
from django.conf import settings

class Artwork(models.Model):
    met_id = models.CharField(max_length=200, blank=True, null=True) 
    object_number = models.CharField(max_length=50, unique=True, null=True)
    artist = models.CharField(max_length=100, blank=True, null=True) # اگر از Met API استفاده میکنی
    title = models.CharField(max_length=400)
    image_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title