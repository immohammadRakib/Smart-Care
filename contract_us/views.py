from django.shortcuts import render
from rest_framework import viewsets
from .models import ContractUs
from .serializers import ContractUsSerializer

# Create your views here.
class ContractUsViewSet(viewsets.ModelViewSet):
    queryset = ContractUs.objects.all()
    serializer_class = ContractUsSerializer