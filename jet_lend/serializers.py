from rest_framework import serializers
from . models import Investor, Passport, Document, Qualification


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Qualification
        fields = '__all__'


class PassportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passport
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = '__all__'

class InvestorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investor
        fields = '__all__' 