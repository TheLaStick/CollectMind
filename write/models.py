from django.contrib.auth.models import User
from django.db import models

class CollectMind(models.Model):
    name = models.CharField(max_length=255)
    time = models.DateTimeField(auto_now_add=True, blank=False)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    end = models.BooleanField(default=False)
    def __str__(self):
        return "{} ({})".format(self.name, self.author.username)

# Create your models here.
