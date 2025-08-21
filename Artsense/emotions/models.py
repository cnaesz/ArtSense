from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from artworks.models import Artwork
from accounts.models import CustomUser


class Response(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='responses')
    word = models.CharField(max_length=64)  # تک‌کلمه؛ محدود کن به طول مناسب
    normalized_word = models.CharField(max_length=64, db_index=True)  # برای جستجو/گروه‌بندی
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['artwork', 'normalized_word']),
        ]