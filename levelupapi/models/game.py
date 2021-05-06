from django.db import models
from .game_type import GameType
from .gamer import Gamer

class Game(models.Model):
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    difficulty = models.IntegerField()
    numberOfPlayers = models.IntegerField()
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)