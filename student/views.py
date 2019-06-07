from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student


def register(request):
     if request.method == "POST":
          form = StudentForm(request.POST or None)
          if form.is_valid():
               try:
                    form.save() 
                    return redirect('student:display')
               except:
                    pass

     else:
          form = StudentForm()
     return render(request,'student/register.html',{'form':form})

def display(request):
     students = Student.objects.all()
     return render(request,'student/display.html',{'students':students})

def update(request,id):
     student = Student.objects.get(sid = id)
     form = StudentForm(request.POST or None,instance = student)
     if form.is_valid():
          form.save()
          return redirect("student:display")
     return  render(request,'student/update.html',{'form':form, 'student':student})

def delete(request,id):
     student = Student.objects.get(sid=id)
     student.delete()
     return redirect('student:display')

          


