from typing import Any
from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import FormView,TemplateView,UpdateView,View
from accounts.forms import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
# Create your views here.



class StuHomeView(TemplateView):
    template_name='sthome.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # user=self.request.user.id
        # context['data']=Student.objects.get(id=user)
        return context


def studentanswer(request,**kwargs):
    if request.user.is_authenticated:
        student = request.user.student_id_id  
        student_answers = StudentAnswer.objects.filter(student=student)
        return render(request, 'exam.html', {'student_answers': student_answers})
    else:
       
        return HttpResponse("Please log in to attend the exam.", status=401)


def submit_exam(request):
    if request.method == 'POST':
        student = request.user.id 
        stu=Student.objects.get(id=student)
        total_score = 0
        for key, value in request.POST.items():
            if key.startswith('answer_'):
                student_answer_id = int(key.split('_')[1])
                answer_id = int(value)
                student_answer = StudentAnswer.objects.get(id=student_answer_id)
                student_answer.answer_id = answer_id
                student_answer.save()
                if student_answer.answer_id == answer_id and student_answer.answer.is_correct:
                        total_score += 1
            sug=Suggestion.objects.all()
            if total_score >= 8:
                stu.category = "Excellent"
                for i in sug:
                   if i.cat.name == "Excellent":
                      stu.suggestion= i.suggestion
                      stu.video=i.video
                      stu.audio=i.audio
            elif total_score >= 6:
                stu.category = "Good"
                for i in sug:
                   if i.cat.name == "Good":
                    stu.suggestion= i.suggestion
                    stu.video=i.video
                    stu.audio=i.audio
            elif total_score>= 4:
                stu.category = "Average"
                for i in sug:
                   if i.cat.name == "Average":
                    stu.suggestion= i.suggestion
                    stu.video=i.video
                    stu.audio=i.audio
            elif total_score >= 2:
                stu.category = "Poor"
                for i in sug:
                   if i.cat.name == "Poor":
                    stu.suggestion= i.suggestion
                    stu.video=i.video
                    stu.audio=i.audio
            else:
                stu.category = "Very Poor"
                for i in sug:
                   if i.cat.name == "Very Poor":
                        stu.suggestion= i.suggestion
                        stu.video=i.video
                        stu.audio=i.audio            
            stu.score = total_score
            stu.save()
            
        return redirect('sh') 
    else:
        return HttpResponse("Invalid request method.", status=405)


class Profile(TemplateView):
   template_name='profile.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs) 
      id=self.request.user
      context['data']=Student.objects.get(std_id=id)
      return context
   
class ProfileUpdateView(UpdateView):
    template_name="profileupdate.html"
    model=Student
    form_class=StudentFormProfile
    success_url=reverse_lazy('pro')


class SugView(TemplateView):
   template_name='sugg.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs) 
      id=self.request.user
      context['data']=Student.objects.get(std_id=id)
      return context
   
class ResultView(TemplateView):
   template_name='result.html'
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs) 
      id=self.request.user
      print(id)
      std=id.id
      print(std)
      context['data']=Student.objects.get(std_id=id)
      context['result']=StudentAnswer.objects.filter(student=std)
      return context

# class Profile(TemplateView):
#    template_name='profile.html'
#    def get_context_data(self, **kwargs):
#       context = super().get_context_data(**kwargs) 

class ChangePasswordView(FormView):
    template_name="changeps.html"
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
        
class LogOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("log")      
    

class Text(TemplateView):
    template_name="text.html"    
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs) 
      id=self.request.user
      context['data']=Student.objects.get(std_id=id)
      return context
    
class Audio(TemplateView):
    template_name="audio.html"    
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs) 
      id=self.request.user
      context['data']=Student.objects.get(std_id=id)
      return context