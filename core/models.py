from django.db import models


class Challenge(models.Model):

    name = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    description = models.TextField()

    class Level(models.IntegerChoices):
        EASY = 1, "easy"
        MEDIUM = 2, "medium"
        HARD = 3, "hard"
        EXTREME = 4, "extreme"
    level = models.IntegerField(choices=Level.choices)

    def __str__(self):
        return f"{self.name}"


