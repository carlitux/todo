
from django.db import models


class Todo(models.Model):

    task = models.TextField(db_index=True)
    done = models.BooleanField(db_index=True, default=False)

    owner = models.ForeignKey('auth.User')

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.task
