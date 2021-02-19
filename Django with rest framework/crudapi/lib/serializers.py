from rest_framework import serializers
from lib.models import book
class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=book
        fields=['id','title','author','isbn','publisher']