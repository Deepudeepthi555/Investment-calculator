from rest_framework import serializers
from .models import Student,expense

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('name','age','email','phone','address','dateofbirth')



class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
        

    class Meta:
         model = expense
         fields = ('student','housingrent','travelexp','foodexp','Utilitybills','Cellphonebill','Groceryexp','Clothingexp','healthinsurance')
