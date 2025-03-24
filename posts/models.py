from django.db import models

# Create your models here.

#TODO mirar que tipos de datos hay
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.IntegerField
    create_at = models.DateTimeField(auto_now_add=True) #Para que se cree con la fecha en la que se inserte