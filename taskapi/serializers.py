from rest_framework import serializers

from task.models import Todos

class TodoSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Todos
        fields="__all__"