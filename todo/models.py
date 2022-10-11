from django.db import models

class Todo(models.Model):
    
    description = models.CharField(max_length=250,unique=True)
    completed = models.BooleanField(default = False)


