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
CBC means Comprehensive Blood Count.
CBCAnalysis is an abstract class because the fields
are common (same name) between the commercial and 
chronus tables.
"""
class CBCAnalysis(models.Model):
    class Meta:
        abstract = True

    blood_sample = models.ForeignKey(
        BloodSample,
        on_delete = models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

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
"""
The Common Comprehensive Metabolic Panel (CMP) Fields.
Note this is an abstract class.
"""
class CMPAnalysis(models.Model):
    class Meta:
        abstract = True

    blood_sample = models.ForeignKey(
        BloodSample,
        on_delete = models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    na_plus = models.FloatField()
    k_plus = models.FloatField()
    tCO2 = models.FloatField()
    cl_minus = models.FloatField()
    glu = models.FloatField()
    ca = models.FloatField()
    bun = models.FloatField()
    cre = models.FloatField()
    alp = models.FloatField()
    ast = models.FloatField()
    tbil = models.FloatField()
    alb = models.FloatField()
    tp = models.FloatField()

    qc = models.FloatField()
    hem = models.FloatField()
    lip = models.FloatField()
    ict = models.FloatField()
class CMPCommercialAnalysis(CMPAnalysis):
    disc_lot_number = models.IntegerField()
    serial_number = models.IntegerField()
class CMPChronusAnalysis(CMPAnalysis):
    pass