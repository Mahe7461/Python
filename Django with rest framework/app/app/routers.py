from emp.viewsets import EmployeeViewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register('emp',EmployeeViewset),
#router.Register('generics',student_name)