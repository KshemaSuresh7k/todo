from django.shortcuts import render
from taskapi.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from task.models import Todos


class TodoViewsetview(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todos.objects.all()