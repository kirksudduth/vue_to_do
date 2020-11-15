from django.db import models

class ToDo(models.Model):

    toDo = models.CharField(max_length=300)
    when = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)