from django.db import models
from django.urls import reverse
import threading
import random
class Game(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gamesearch', args=[str(self.slug)])



