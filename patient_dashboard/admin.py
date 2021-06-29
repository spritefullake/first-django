from django.contrib import admin
from .models import Patient, BloodSample, \
                    CommercialCBC, ChronusCBC, \
                    CommercialCMP, ChronusCMP
# Register your models here.
admin.site.register(Patient)
admin.site.register(BloodSample)
admin.site.register(CommercialCBC)
admin.site.register(ChronusCBC)
admin.site.register(CommercialCMP)
admin.site.register(ChronusCMP)