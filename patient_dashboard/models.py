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
"""
Analysis is an abstract class because the fields
are common (same name) between the commercial and 
chronus tables
"""
class CBCAnalysis(models.Model):
    class Meta:
        abstract = True

    wbc = models.FloatField()
    neu = models.FloatField()
    lym = models.FloatField()
    mono = models.FloatField()
    eos = models.FloatField()
    baso = models.FloatField()

    rbc = models.FloatField()
    hgb = models.FloatField()
    hct = models.FloatField()
    mcv = models.FloatField()
    mch = models.FloatField()
    mchc = models.FloatField()
    rdw = models.FloatField()

    plt = models.FloatField()
    mpv = models.FloatField()
    pct = models.FloatField()
    pdw = models.FloatField()

class CommercialAnalysis(CBCAnalysis):
    pass
class ChronusAnalysis(CBCAnalysis):
    pass
class CMPAnalysis(models.Model):
    class Meta:
        abstract = True
    pass
class CMPCommercialAnalysis(CMPAnalysis):
    pass
class CMPChronusAnalysis(CMPAnalysis):
    pass