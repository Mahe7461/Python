from rest_framework import viewsets, generics
from . import models
from django.contrib.auth.models import User
from . import seralizers
class student_name(viewsets.GenericViewSet):
    queryset=User.objects.all()
    seralizers_class= seralizers.stu
    def get_queryset(self):
        User=self.request.user
        return User.accounts.all()


