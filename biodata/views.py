from django.shortcuts import render
from .Serializers import ExpenseSerializer, StudentSerializer
from .models import Student,expense
from rest_framework import viewsets
# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = expense.objects.all()
    serializer_class = ExpenseSerializer