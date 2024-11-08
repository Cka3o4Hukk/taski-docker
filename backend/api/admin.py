"""Модуль администратора для управления задачами в интерфейсе Django."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Класс администратора для модели Task."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
