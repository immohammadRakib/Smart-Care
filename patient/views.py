from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import PatientSerializer, RegistrationSeralizer
from .models import Patient
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
#for email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.shortcuts import redirect

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
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            emai_subject = 'Confirm Your Email'

            emai_body = render_to_string('confirm_email.html', {'confirm_link': confirm_link}) 
            email = EmailMultiAlternatives(emai_subject, '', to=[user.email])
            email.attach_alternative(emai_body, 'text/html')
            email.send()

            return Response('Check Your Email')
        return Response(serializer.errors)
    

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)    
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()    
        return redirect('register')
    else:
        return redirect('register')


