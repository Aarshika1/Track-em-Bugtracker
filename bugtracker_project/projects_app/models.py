from django.db import models
from django import forms
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)
    organization_name = models.CharField(max_length=70)
    sector = models.CharField(max_length=50)
    technology = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name
