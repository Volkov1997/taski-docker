"""Что-то."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Что-то."""

    class Meta:
        """Что-то."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
