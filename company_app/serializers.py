from rest_framework import serializers
from company_app import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'