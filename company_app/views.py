from django.shortcuts import render
from rest_framework import viewsets
from company_app import models
from company_app import serializers

# Create your views here.
class EmployeeViewset(viewsets.ModelViewSet):
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()