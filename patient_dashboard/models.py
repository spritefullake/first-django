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

class BloodSample(models.Model):
    patient = models.ForeignKey(
        Patient,
        on_delete = models.CASCADE
    )
    vessel_type = models.TextField()
    collection_date = models.DateTimeField()
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # blood draw fields:
    temperature = models.FloatField()
    spO2 = models.FloatField()
    heart_rate = models.FloatField()
    blood_pressure = models.FloatField()
    weight = models.FloatField() #should this go to patient?
    blood_draw_volume = models.FloatField()

class CommercialAnalysis(models.Model):
    pass
class ChronusAnalysis(models.Model):
    pass
class CMPCommercialAnalysis(models.Model):
    pass
class CMPChronusAnalysis(models.Model):
    pass