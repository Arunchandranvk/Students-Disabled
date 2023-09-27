from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .models import Question
from .forms import *
from django.views.generic import FormView,CreateView,UpdateView,TemplateView
from django.contrib.auth import authenticate,login
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password

# Create your views here.

import pandas as pd
import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_save, sender=Student)
def create_user_from_student(sender, instance, created, **kwargs):
    if created:
        # User = get_user_model()
        CustUser= get_user_model()
        student_id_id=instance.id
        username = instance.std_id
        password = 'admin@123'  # Set your desired default password here
        # User.objects.create_user(username=username, password=password)
        CustUser.objects.create_user(username=username, password=password,student_id_id=student_id_id)

class LoginView(FormView):
    template_name="login.html"
    form_class=LogForm
    def post(self,request,*args,**kwargs):
        log_form=LogForm(data=request.POST)
        if log_form.is_valid():  
            us=log_form.cleaned_data.get('username')
            ps=log_form.cleaned_data.get('password')
            user=authenticate(request,username=us,password=ps)
            if user: 
                login(request,user)
                if request.user.is_superuser == 1:
                    return redirect('h')
                else:
                    return redirect('sh')
            else:
                return render(request,'login.html',{"form":log_form})
        else:
            return render(request,'login.html',{"form":log_form})  

    

class AddStudent(CreateView):
    template_name='addstudent.html'
    model=Student
    form_class=StudentForm 
    success_url=reverse_lazy('stu')  
    



class QuestView(TemplateView):
    template_name='test.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id=kwargs.get('pk')
        context['stu']=Student.objects.get(id=id)
        context['ques']=Question.objects.all()
        return context 
    
class QuestViewAll(TemplateView):
    template_name='testall.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stu']=Student.objects.all()
        context['ques']=Question.objects.all()
        return context     

def Test(request,**kwargs):
    if request.method == 'POST':
        id=kwargs.get('pk')
        stu=Student.objects.get(id=id)
        que=Question.objects.all()
        assignment = StudentAnswer(student=stu, question=que)
        assignment.save()
        return redirect('det')    


def AssignView(request,**kwargs):
    if request.method == 'POST':
        # Get all available tests
        tests = Question.objects.all()

        # Get all students
        students = Student.objects.all()

        # Assign all tests to all students
        for test in tests:
            for student in students:
                assignment, created = StudentAnswer.objects.get_or_create(student=student, question=test)
                if created:
                    assignment.save()

        # Redirect to a success page or any other appropriate page
        return redirect('h')  # Replace 'success_page' with the actual URL name

    # Retrieve all available tests
    tests = Question.objects.all()

    return render(request, 'testall.html', {'tests': tests})          
 
   
