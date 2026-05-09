from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_displayj = ['doctor_name', 'patient_name', 'symptom', 'time', 'cancel', 'appointment_type', 'appointment_status']
    def patient_name(self,obj):
        return obj.patient.user.first_name
    
    def doctor_name(self, obj):
        return obj.doctor.user.first_name

admin.site.register(Appointment, AppointmentAdmin)