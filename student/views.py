from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm
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
