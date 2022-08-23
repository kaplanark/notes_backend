from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    img = models.URLField()
    title = models.CharField(max_length=5000)
    text = models.CharField(max_length=15000)
    color = models.CharField(max_length=200)
    categories = models.CharField(max_length=500)
    show = models.BooleanField()
    pinned = models.BooleanField()
    archived = models.BooleanField()
    trashed = models.BooleanField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.task