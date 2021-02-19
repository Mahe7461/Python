from .views import UserViewSet,GroupViewSet
from django.urls import path



urlpatterns = [
    path('api/register/', GroupViewSet(), name='register'),
     path('api/login/',UserViewSet(), name='login'),
]