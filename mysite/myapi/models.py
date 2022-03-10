from django.db import models

# Create your models here.
class Rapper(models.Model):
    name = models.CharField(max_length=100)
    aka = models.CharField(max_length=60)



class Music(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)


def __str__(self):
    return self.aka


def __mus__(self):
    return self.genre