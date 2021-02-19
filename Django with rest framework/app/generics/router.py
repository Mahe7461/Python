from rest_framework import routers
from generics.viewsets import student_name
router = routers.DefaultRouter()
router.register('generics',student_name)