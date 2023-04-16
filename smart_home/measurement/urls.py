from django.urls import path
from .views import MeasurementAPIList, SensorAPIList, SensorAPIRetrieveUpdate

urlpatterns = [
    path('measurement/', MeasurementAPIList.as_view()),
    path('sensor/', SensorAPIList.as_view()),
    path('sensors/<int:pk>/', SensorAPIRetrieveUpdate.as_view())
]