from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Department
from .serializers import UserSerializer, DepartmentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

