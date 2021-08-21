from .models import Human
from rest_framework import serializers

class HeroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Human
        fields = ('name', 'contact','college','year','branch','nlp')


    