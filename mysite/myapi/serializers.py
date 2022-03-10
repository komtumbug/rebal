from rest_framework import serializers
from .models import Music, Rapper

class RapperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rapper
        fields = ('name','aka')


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Music
        fields = ('name','genre')