from rest_framework import serializers
from .models import students
class stu(serializers.ModelSerializer):
    class Meta:
        fleid ='__all__'