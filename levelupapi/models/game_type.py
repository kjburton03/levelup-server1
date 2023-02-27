from django.db import models
# from django.contrib.auth.models import User

class GameType(models.Model):

    genre = models.CharField(max_length=69)
    