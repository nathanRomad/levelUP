from django.db import models
from .gamer import Gamer
from .event import Event

class Player(models.Model):
    gamer : models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event : models.ForeignKey(Event, on_delete=models.CASCADE)