from django.db import models

# Create your models here.

class Student(models.Model):
    Roll_no=models.PositiveIntegerField()
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.EmailField(max_length=100)
    Degree=models.CharField(max_length=30)
    CGPA=models.FloatField()

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}"