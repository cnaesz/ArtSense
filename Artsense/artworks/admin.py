from django.contrib import admin

# Register your models here.
from .models import Artwork



class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'met_id')
    search_fields = ('title', 'artist')
    list_filter = ('created_at',)



admin.site.register(Artwork, ArtworkAdmin)