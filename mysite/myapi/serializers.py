from rest_framework import serializers
from .models import Car, Crypto, Music, Rapper, Games, Plant

class RapperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rapper
        fields = ('name','aka')


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ('name','genre')


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('name',"color")



class CryptoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model : Crypto
        fields = ('name','vol')


class GamesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model : Games
        fields = ("name",'type')


class PlantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model : Plant
        fields = ("name","color")