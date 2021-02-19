from first_app.views import UserViewSet,GroupViewSet
from rest_framework import routers
from first_app import views, urls

router = routers.DefaultRouter()
router.register('users', views.UserViewSet),
router.register('groups', views.GroupViewSet)
