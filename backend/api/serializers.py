"""Сериализатор модели Task."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Настройка сериализатора для модели Task."""

    class Meta:
        """Дополнительные параметры."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
