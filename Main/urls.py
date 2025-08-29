from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DepartmentViewSet, EmployeeViewSet, LeaveRequestViewSet, DepartmentChangeRequestViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'leave-requests', LeaveRequestViewSet)
router.register(r'department-change-requests', DepartmentChangeRequestViewSet)

urlpatterns = router.urls

