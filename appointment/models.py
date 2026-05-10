from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime

# Create your models here.
Appointment_TYPE = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running')
]

Appointment_STATUS = [
    ('Offline', 'Offline'),
    ('Online', 'Online')
]


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(choices=Appointment_TYPE, max_length=10)
    appointment_status = models.CharField(choices=Appointment_STATUS, default='Pending', max_length=10)
    symptom = models.TextField(max_length=100)
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
