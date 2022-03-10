from pyexpat import model
from django.db import models

# Create your models here.
class Rapper(models.Model):
    name = models.CharField(max_length=100)
    aka = models.CharField(max_length=60)



class Music(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)


class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)    


class Crypto(models.Model):
    name = models.CharField(max_length=100)
    vol = models.CharField(max_length=999999999999999)



class Games(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class Plant(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
def __str__(self):
    return self.aka


def __mus__(self):
    return self.genre


def __car__(self):
    return self.color


def __cry__(self):
    return self.name
    

def __gem__(self):
    return self.type


def __pla__(self):
    return self.color