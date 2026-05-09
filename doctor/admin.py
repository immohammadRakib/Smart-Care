from django.contrib import admin
from .models import Doctor, Designation, AvailableTime, Specialization

# Register your models here.
class SpeacializationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

class DesignationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}

admin.site.register(Doctor)
admin.site.register(Designation)
admin.site.register(AvailableTime)
admin.site.register(Specialization)
