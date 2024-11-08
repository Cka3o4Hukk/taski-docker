"""Модуль представлений для управления задачами в API.

Этот модуль содержит представления для модели Task, включая
все стандартные операции CRUD (создание, чтение, обновление,
удаление) с использованием Django REST Framework.
"""
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """Представление для модели Task.

    Этот класс предоставляет стандартные операции CRUD для
    модели Task, используя сериализатор TaskSerializer.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """Удаляет объект задачи и возвращает его данные.

        Переопределяет метод destroy для возврата данных
        удаляемой задачи в ответе.
        """
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
