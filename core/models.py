from django.conf import settings
from django.contrib.auth.models import User
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


class WorkDay(models.Model):
    day = models.CharField(default="", max_length=15)

    def __str__(self):
        return self.day


class TheTypeOfFood(models.Model):
    title = models.CharField(max_length=100)


class Business(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='business',
                                default=None)
    phone = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    days = models.ManyToManyField(WorkDay, blank=True)
    location = models.CharField(max_length=20)
    start_hour = models.TimeField(default="08:00")
    end_hour = models.TimeField(default="16:00")
    TheTypeOfFood = models.ManyToManyField(TheTypeOfFood, blank=True)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return self.user


class UserInChallenge(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='userChallenge')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name='userChallenge')
