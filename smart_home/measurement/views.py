from rest_framework import generics
from .serializers import MeasurementSerializer, SensorDetailSerializer
from .models import Sensor, Measurement


class MeasurementAPIList(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorAPIList(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorAPIRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer