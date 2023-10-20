from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .models import Question
from .forms import *
from django.views.generic import FormView,CreateView,UpdateView,TemplateView,View
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import Suggestion
from student_app.forms import ChangePasswordForm
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
 
class Quesdel(CreateView):
    template_name="quesdel.html"
    model=Question
    form_class=QuesForm
    success_url=reverse_lazy('qans')
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['tests']=Question.objects.all()
        return context 
     
class QuesUpdate(UpdateView):
    template_name="questionupdate.html"
    model=Question
    form_class=QuesForm
    success_url=reverse_lazy('qdel') 
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['tests']=Question.objects.all()
        return context     
 
class QuesAnsUpdView(CreateView):
    template_name="quesansupdate.html"
    model=Answer
    form_class=QuesAnsForm
    success_url=reverse_lazy('qdel')   

class DeleteView(View):
    def get(self,req,*args,**kwargs):
       id=kwargs.get('pk')
       dl=Question.objects.get(id=id)
       dl.delete()
       return redirect('qdel')
    
# class Quesdel(TemplateView):
#     template_name="quesdel.html"
#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context['tests']=Question.objects.all()
#         return context

class SugView(TemplateView):
    template_name="suggestions.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data']=Suggestion.objects.all().order_by('cat')
        return context

class SuggTextView(CreateView):
    template_name="suggtext.html"
    model=Suggestion
    form_class=SugForm
    success_url=reverse_lazy('st')



class SuggVideoView(CreateView):
    template_name="suggvideo.html"
    model=Suggestion
    form_class=SugVideoForm
    success_url=reverse_lazy('sv')

class SuggAudioView(CreateView):
    template_name="suggaudio.html"
    model=Suggestion
    form_class=SugAudioForm
    success_url=reverse_lazy('sadd')




def view_video(request, video_id):
    video = get_object_or_404(Suggestion, pk=video_id)
    video_path = video.video.path
    response = FileResponse(open(video_path, 'rb'))  # Adjust content_type as needed
    return response


def view_videoo(request, videoo_id):
    video = get_object_or_404(Student, pk=videoo_id)
    video_path = video.video.path
    response = FileResponse(open(video_path, 'rb'))  # Adjust content_type as needed
    return response




def play_audio(request, audio_id):
    audio_recording = get_object_or_404(Suggestion, pk=audio_id)
    audio_file = audio_recording.audio
    response = FileResponse(open(audio_file.path, 'rb'))
    return response

def play_audioo(request, audio_id):
    audio_recording = get_object_or_404(Student, pk=audio_id)
    audio_file = audio_recording.audio
    response = FileResponse(open(audio_file.path, 'rb'))
    return response


class DeleteViewSug(View):
    def get(self,req,*args,**kwargs):
       id=kwargs.get('pk')
       dl=Suggestion.objects.get(id=id)
       dl.delete()
       return redirect('sadd')
    

class ChangePasswordViewHome(FormView):
    template_name="changepshome.html"
    form_class=ChangePasswordForm
    def post(self,request,*args,**kwargs):
        form_data=ChangePasswordForm(data=request.POST)
        if form_data.is_valid():
            current=form_data.cleaned_data.get("current_password")
            new=form_data.cleaned_data.get("new_password")
            confirm=form_data.cleaned_data.get("confirm_password")
            user=authenticate(request,username=request.user.username,password=current)
            if user:
                if new==confirm:
                    user.set_password(new)
                    user.save()
                    logout(request)
                    return redirect("log")
                else:
                    return redirect("cp")
            else:
                return redirect("cp")
        else:
            return render(request,"changepassword.html",{"form":form_data})    
        

class SuggestionUpdateView(UpdateView):
    template_name='suggestionupdate.html'
    model=Suggestion
    form_class=SuggestionForm
    success_url=reverse_lazy('sadd')        