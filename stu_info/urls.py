from django.contrib import admin
from django.urls import path 
from.import views

urlpatterns = [
    path('students/',views.index,name='index'),
    path('home/', views.home, name='home'),
    path('students/add_student/',views.add_student,name='add_student'),
    path('students/edit_student/<int:stu_id>',views.edit_student,name='edit_student'),
    path('students/delete_student/<int:stu_id>',views.delete_student,name='delete_student'),
    path('students/update_stu/',views.update,name='update_stu'),
    path('students/view_student/<int:stu_id>',views.view_student,name='view_student'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('students/edit_view',views.edit_view,name='edit_view'),
    
]