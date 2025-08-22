from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'departments', DepartmentViewSet)

urlpatterns = router.urls

