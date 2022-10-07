from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from .models import Student
from .models import Student
from django.shortcuts import redirect

# Create your views here.
def index(request):
   stud=Student.objects.all()
   context = {
      'stud':stud
   }
   return render(request,'index.html',context)


def add_student(request):
   if request.method=='POST':
      name=request.POST.get('name')
      standard =request.POST.get('standard')
      roll_no=int(request.POST.get('roll_no'))
      phone=int(request.POST.get('phone'))
      email=request.POST.get('email')
      if len(request.FILES)!=0:
        image=request.FILES['image'] 
      new_stu=Student(name=name,roll_no=roll_no,standard=standard,phone=phone,image=image,email=email)
      new_stu.save()
      return redirect('add_student')
   return render(request,'add_student.html')

def edit_student(request,stu_id=0): 
   student_detail=Student.objects.get(id=stu_id)

   context = {
      'student_detail':student_detail
   }    
   return render(request,'edit_student.html',context)


def delete_student(request, stu_id=0):
   if stu_id:
      try:
         stu_to_be_removed = Student.objects.get(id=stu_id)
         stu_to_be_removed.delete()
         return redirect('index')
      except:
       return HttpResponse('failed')


def update(request):
    if request.method=='POST':
      stu_id = request.POST.get('stu_id')
      student = Student.objects.get(id = stu_id)
      student.name = request.POST.get('name')
      student.standard = request.POST.get('standard')
      student.roll_no = int(request.POST.get('roll_no'))
      student.email = request.POST.get('email')
      student.phone = int(request.POST.get('phone'))
      student.image=request.FILES['image']
      student.save()
      return redirect('index')

def view_student(request,stu_id=0): 
   student_detail=Student.objects.get(id=stu_id)

   context = {
      'student_detail':student_detail
   }    
   return render(request,'view_student.html',context)
