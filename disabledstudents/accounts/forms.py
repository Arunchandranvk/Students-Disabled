from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *



class LogForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control","style":"border-radius: 0.75rem; "}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control","style":"border-radius: 0.75rem; "}))




class StudentForm(forms.ModelForm):
     class Meta:
          model=Student
          exclude=['score','category','suggestion']
          widgets={
               'std_id':forms.TextInput(attrs={"placeholder":"Student Id","class":"form-control","style":"border-radius: 0.75rem; "}),
               'gender':forms.RadioSelect(),
               'age':forms.NumberInput(attrs={"placeholder":"Age","class":"form-control","style":"border-radius: 0.75rem; "}),
          }

class UserRegForm(UserCreationForm):
     class Meta:
          model=User
          fields=['username','password1']          


     

