from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CarSerializer, GamesSerializer, RapperSerializer,MusicSerializer,CryptoSerializer,PlantSerializer
from .models import Rapper,Music,Car,Crypto,Games, Plant




class RapperViewSet(viewsets.ModelViewSet):
    queryset = Rapper.objects.all().order_by('aka')
    serializer_class = RapperSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all().order_by('genre')
    serializer_class = MusicSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('color')
    serializer_class = CarSerializer


class CryptoViewSet(viewsets.ModelViewSet):
    queryset = Crypto.objects.all().order_by('name')
    serializer_class = CryptoSerializer


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all().order_by('type')
    serializer_class = GamesSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all().order_by('color')
    serializer_class = PlantSerializer