from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from .serializers import *
from api import heart

class ReviewApiView(APIView):
    def get(self,request):
        v=Review.objects.all()
        serializer=ReviewSerializer(v,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class HeartApiView(APIView):
    def get(self,request):
        v=Heart.objects.all()
        serializer=HeartSerializer(v,many=True)
        return Response(serializer.data)

    def post(self,request):
        print(request.data)
        serializer=HeartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            queryset=Heart.objects.order_by("id")
            ob=Heart.objects.latest("id")
            pre=heart.prediction(ob)
            return Response({"status":"Success","Survived":pre})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class LogApiView(APIView):
    def get(self,request,username):
        user=Cust.objects.get(username=username)
        serializer=CustSerializer(user)
        return Response(serializer.data)

    def put(self,request,username):
        user=Cust.objects.get(username=username)
        serializer=CustSerializer(user,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,username):
        user=Cust.objects.get(username=username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CustApiView(APIView):
    def get(self,request):
        v=Cust.objects.all()
        serializer=CustSerializer(v,many=True)
        return Response(serializer.data)

    def post(self,request):
        print("=========================================================")
        print(request.data)
        data=request.data
        serializer=CustSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
