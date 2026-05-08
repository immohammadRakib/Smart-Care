from django.contrib import admin
from .models import ContractUs

# Register your models here.
class ContractModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'problem']
admin.site.register(ContractUs, ContractModelAdmin)

