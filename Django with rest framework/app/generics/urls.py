from django.urls import path,include
from .router import router
urlpatterns = [
    path('generic',include(router.urls))
]
