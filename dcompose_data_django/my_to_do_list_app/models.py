from django.db import models
from autoslug import AutoSlugField

# I have created model class for creating database table 

class ToDoList(models.Model):

    title = models.CharField(max_length=255, default=None, null=False, unique=True)
    description = models.TextField(default=None, null=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', default=None, null=False, unique=True)

    class Meta:
        verbose_name = 'To Do Task'
        verbose_name_plural = 'To Do List'

    def __str__(self):
        return self.title