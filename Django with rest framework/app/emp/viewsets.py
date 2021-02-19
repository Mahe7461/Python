from rest_framework import viewsets, generics
from . import models
from . import serilazers



class EmployeeViewset(viewsets.ModelViewSet):
    queryset=models.Empolyeeclass.objects.all()
    serializer_class=serilazers.emp_name
    