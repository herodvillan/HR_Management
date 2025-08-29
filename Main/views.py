from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Department
from .serializers import UserSerializer, DepartmentSerializer
from .models import Employee #2
from .serializers import EmployeeSerializer
from .models import LeaveRequest #3
from .serializers import LeaveRequestSerializer
from .models import DepartmentChangeRequest #4
from .serializers import DepartmentChangeRequestSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

#phase two
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#phase three
class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer

#phase four
class DepartmentChangeRequestViewSet(viewsets.ModelViewSet):
    queryset = DepartmentChangeRequest.objects.all()
    serializer_class = DepartmentChangeRequestSerializer

