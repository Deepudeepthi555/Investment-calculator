from rest_framework import serializers
from .models import Student,expense

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('name','age','email','phone','address','dateofbirth')

