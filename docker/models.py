from django.db import models
from django.urls import reverse


# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date created')
    finished = models.BooleanField()

    def get_absolute_url(self):
        return reverse('todo-list')

    def __str__(self):
        return f"{self.name}, published: {self.pub_date}, finished: {self.finished}"
