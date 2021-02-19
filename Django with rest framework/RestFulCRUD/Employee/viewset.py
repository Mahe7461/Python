from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import generics


class EmployeeViewset(viewsets.ModelViewSet):
    queryset=models.Employee.objects.all()
    serializer_class=serializers.EmployeeSerializer