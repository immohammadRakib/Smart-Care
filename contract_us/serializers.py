from rest_framework import serializers
from .models import ContractUs

class ContractUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractUs
        fields = '__all__'