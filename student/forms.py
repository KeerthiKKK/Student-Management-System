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
        

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username=forms.CharField(max_length=150,label="Username")
    password=forms.CharField(widget=forms.PasswordInput,label="Password")

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,label="Password")
    confirm_password=forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model=User
        fields=["username","email"]

    def clean(self):
        cleaned_data = super().clean()
        password=cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")