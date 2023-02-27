from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):

    name = models.CharField(max_length=69)
    date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False) 
    location = models.CharField(max_length=200)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)

    attendees = models.ManyToManyField('Gamer', through='EventAttendees')

    

