from django.db import models
from .gameType import GameType

class Game(models.Model):
    title = models.CharField(max_length=50)
    difficulty = models.IntegerField()
    numberOfPlayers = models.IntegerField()
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)