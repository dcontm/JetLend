from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.


class QualificationViewSet(viewsets.ModelViewSet):
	queryset = models.Qualification.objects.all()
	serializer_class = serializers.QualificationSerializer

class PassportViewSet(viewsets.ModelViewSet):
	queryset = models.Passport.objects.all()
	serializer_class = serializers.PassportSerializer

class DocumentViewSet(viewsets.ModelViewSet):
	queryset = models.Document.objects.all()
	serializer_class = serializers.DocumentSerializer

class InvestorViewSet(viewsets.ModelViewSet):
	queryset = models.Investor.objects.all()
	serializer_class = serializers.InvestorSerializer

