from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Department, Employee, LeaveRequest, DepartmentChangeRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

#phase two
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'user', 'department', 'position', 'date_joined']

#phase three

class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = ['id', 'employee', 'start_date', 'end_date', 'reason', 'approved']

#phase four

class DepartmentChangeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentChangeRequest
        fields = ['id', 'employee', 'requested_department', 'reason', 'approved']

