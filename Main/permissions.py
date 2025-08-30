from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:  # HR/Admin
            return True
        return obj.user == request.user or obj.employee.user == request.user

