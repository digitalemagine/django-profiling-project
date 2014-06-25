from django.db import models
from jsonfield import JSONBField, JSONCharField

# Create your models here.

class JSONModel(models.Model):
    json = JSONBField()

class JSONCharModel(models.Model):
    json = JSONCharField(max_length=255)

class CharModel(models.Model):
    json = models.CharField(max_length=255)