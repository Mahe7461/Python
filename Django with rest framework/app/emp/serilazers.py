from rest_framework import serializers
from .models import  Empolyeeclass
class emp_name(serializers.ModelSerializer):
    class Meta:
        model= Empolyeeclass
        fields='__all__'
