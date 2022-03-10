from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RapperSerializer,MusicSerializer
from .models import Rapper,Music




class RapperViewSet(viewsets.ModelViewSet):
    queryset = Rapper.objects.all().order_by('aka')
    serializer_class = RapperSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all().order_by('genre')
    serializer_class = MusicSerializer