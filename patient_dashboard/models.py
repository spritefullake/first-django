from django.conf import settings
from django.db import models
from django.utils import timezone

class Patient(models.Model):
    age = models.IntegerField()
    date_of_birth = models.DateField()
    height = models.FloatField()
    ethnicity = models.TextField()
    gender = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.age}"