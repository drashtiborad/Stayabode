from django.db import models
from django_mysql.models import EnumField


class TodoList(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()
    todo_time = models.DateTimeField()
    status = EnumField(choices=['In Progress', 'Completed', 'Pending'])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'todo_list'
