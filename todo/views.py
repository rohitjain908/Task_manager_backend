from django.shortcuts import render

# Create your views here.

from .models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets

class Todoview(viewsets.ModelViewSet):
  serializer_class=TodoSerializer
  queryset=Todo.objects.all()
  

