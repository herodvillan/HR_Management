from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Department
from .models import Employee #2


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
