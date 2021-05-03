from django.db import models
from .game import Game
from .gamer import Gamer

class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    host = models.ForeignKey(Gamer, on_delete=models.CASCADE)