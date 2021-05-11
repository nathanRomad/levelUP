from django.db import models
from .game import Game


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    host = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField(
        "Gamer", through="Player", related_name="attending")

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
