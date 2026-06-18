from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics
from services.permissions import IsAdminUserRole

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    
class EmployeeCreateView(
    generics.CreateAPIView
):

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer

    permission_classes = [
        IsAdminUserRole
    ]

class EmployeeManageView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer

    permission_classes = [
        IsAdminUserRole
    ]