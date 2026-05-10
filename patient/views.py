from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import PatientSerializer, RegistrationSeralizer
from .models import Patient
from rest_framework.response import Response


# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class RegistrationAPIView(APIView):
    serializer_class = RegistrationSeralizer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response('Done')
        return Response(serializer.errors)
