
from django.db import models

from .querysets import TodoQuerySet


class Todo(models.Model):  # pragma: no cover

    task = models.TextField(db_index=True)
    done = models.BooleanField(db_index=True, default=False)

    objects = TodoQuerySet.as_manager()

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.task
