from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    shortDescription = models.TextField()
    description = models.TextField()
    technologies = models.CharField(max_length=100)
    image = models.FilePathField(path="app\static\img")