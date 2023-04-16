from django.contrib import admin
from .models import Measurement, Sensor
# Register your models here.
admin.site.register(Measurement)
admin.site.register(Sensor)