from django.db import models

# Create your models here.
class Student(models.Model):
    name =models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    address=models.TextField()
    dateofbirth=models.DateField()
    def __str__(self):
        return self.name 

class expense(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    housingrent = models.DecimalField(max_digits=10,decimal_places=2)
    travelexp = models.DecimalField(max_digits=10,decimal_places=2)
    foodexp = models.DecimalField(max_digits=10,decimal_places=2)
    Utilitybills = models.DecimalField(max_digits=10,decimal_places=2)
    Cellphonebill = models.DecimalField(max_digits=10,decimal_places=2)
    Groceryexp = models.DecimalField(max_digits=10,decimal_places=2)
    Clothingexp = models.DecimalField(max_digits=10,decimal_places=2)
    healthinsurance = models.DecimalField(max_digits=10,decimal_places=2)

