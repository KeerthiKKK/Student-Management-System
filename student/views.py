from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm,LoginForm,RegistrationForm
# Create your views here.
def index(request):
    return render(request,"students/index.html",{
        "students":Student.objects.all()
    })

def view_student(request,id):
    student=Student.objects.all(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_Roll_no = form.cleaned_data['Roll_no']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_Degree = form.cleaned_data['Degree']
            new_CGPA = form.cleaned_data['CGPA']

            new_student = Student(
                Roll_no=new_Roll_no,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                Degree=new_Degree,
                CGPA=new_CGPA
            )
            new_student.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})

def edit(request,id):
    if request.method =='POST':
        student = Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return render(request,'students/edit.html',{
                'form':form,
                'success':True
            })
    else:
        student = Student.objects.get(pk=id)
        form=StudentForm(instance=student)
    return render(request,"students/edit.html",{
        'form':form
    })

def delete(request,id):
    if request.method=='POST':
        student=Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request):
    if request.method =="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.error(request,"Invalid credentials")
                #form.add_error(None,"Invalid uname and password")

    else:
        form=LoginForm()
    return render(request,"students/login.html",{'form':form})


def register_view(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,'students/registration.html',{'form':form})