import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Competitor(models.Model):
    name = models.CharField(max_length=100)
    registration_number = models.IntegerField(max_length=10)

    def __str__(self):
        return self.name
    
    @classmethod
    def create(cls, name, registration_number):
        competitor = cls(name = name, registration_number = registration_number)
        return competitor

