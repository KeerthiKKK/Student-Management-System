from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=["Roll_no","first_name","last_name","email","Degree","CGPA"]
        labels={"Roll_no":"Student Roll.No",
                "first_name":"FirstName",
                "last_name":"LastName",
                "email":"EmailID",
                "Degree":"Degree",
                "CGPA":"CGPA"}
        widgets = {
                'Roll_no': forms.NumberInput(attrs={'class': 'form-control'}),
                'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                'Degree': forms.TextInput(attrs={'class': 'form-control'}),
                'CGPA': forms.NumberInput(attrs={'class': 'form-control'}),
                }