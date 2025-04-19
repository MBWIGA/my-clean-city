from django.db import models

# Create your models here.
class Citizen(models.Model):
    name = models.Charfield(max_length=255)