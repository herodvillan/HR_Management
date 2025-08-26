from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Department
from .serializers import UserSerializer, DepartmentSerializer
from .models import Employee #2
from .serializers import EmployeeSerializer

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
