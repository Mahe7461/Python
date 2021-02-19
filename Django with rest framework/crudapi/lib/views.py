from django.shortcuts import render
from rest_framework import generics
from lib.serializers import bookserializer
from lib.models import book
# Create your views here.
class booklist(generics.ListCreateAPIView):
    queryset = book.objects.all()
    serializer_class=bookserializer
class bookdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = book
    serializer_class = bookserializer

