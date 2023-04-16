from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    id_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')
    temperature = models.DecimalField(max_digits=5, decimal_places=1)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"id_sensor: {self.id_sensor}, temperature: {self.temperature}, date: {self.date}"