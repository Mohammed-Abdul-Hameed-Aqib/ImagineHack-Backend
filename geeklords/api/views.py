from django.shortcuts import render
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Human


class HumanViewSet(viewsets.ModelViewSet):
    queryset = Human.objects.all().order_by('name')
    serializer_class = HeroSerializer
# Create your views here.
