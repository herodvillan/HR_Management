from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DepartmentViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls

