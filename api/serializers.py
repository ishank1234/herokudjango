from .models import *
from .views import *
from rest_framework import serializers

class CustSerializer(serializers.ModelSerializer):

    class Meta:
        model=Cust
        fields=['name','age','email','gender','username','password']

class HeartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Heart
        fields="__all__"
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields="__all__"
