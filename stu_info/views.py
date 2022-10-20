from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .models import Student
from django.shortcuts import redirect
import os

# Create your views here.
def index(request):
   # del request.session['student_id']
   if 'student_id' not in request.session:
      return redirect('signin')
   else:
      student_id = request.session['student_id']
      stud=Student.objects.filter(id=student_id)
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
      # if len(request.FILES)!=0:
      #      os.remove(student.image.path)
      if len(request.FILES)!=0:
       student.image=request.FILES['image']

      student.save()
      return redirect('index')

def view_student(request,stu_id=0): 
   student_detail=Student.objects.get(id=stu_id)

   context = {
      'student_detail':student_detail
   }    
   return render(request,'view_student.html',context)

def home(request):
    return render(request,'home.html')


def signup(request):
    if request.method=='POST':
      name = request.POST.get('name')
      username=request.POST.get('username')
      password=request.POST.get('password')
      phone=request.POST.get('mobile')
      email=request.POST.get('email')
      gender=request.POST.get('gender') 
      new_stu=Student(name=name,username=username,password=password,phone=phone,email=email,gender=gender)
      new_stu.save()
      messages.info(request, 'Signup successfully!')
      return redirect('home')
    return render(request,'signup.html')

def signin(request):
   if 'student_id' not in request.session: 
      return render(request, 'login.html')
   else:
      return redirect('index')
   


def login(request):
       if request.method == 'POST':
       # AuthenticationForm_can_also_be_used__
         email = request.POST.get('email')
         password = request.POST.get('password')
         
         if Student.objects.filter(email=email, password=password).exists():
            student_detail = Student.objects.filter(email=email).first()
            #session set
            request.session['student_id'] = student_detail.id
            request.session['student_email'] = student_detail.email

            messages.info(request, 'Login successfully!')
            return redirect('index')
         else:
            messages.info(request,'user not register')
            return redirect('/sigin/')
         
     
def logout(request):
    try:
        del request.session['student_id']
        return redirect('signin')
    except:
        pass
    return HttpResponse("You're logged out.")


def edit_view(request):
   if request.method=='POST':
      stu_id = request.POST.get('stu_id')
      student = Student.objects.get(id = stu_id)
      student.name = request.POST.get('name')
      student.standard = request.POST.get('standard')
      student.roll_no = int(request.POST.get('roll_no'))
      student.email = request.POST.get('email')
      student.phone = int(request.POST.get('phone'))
      if len(request.FILES)!=0:
           os.remove(student.image.path)
      if len(request.FILES)!=0:
       student.image=request.FILES['image']

      student.save()
      return redirect('index')   

