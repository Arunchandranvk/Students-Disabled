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
          exclude=['score','category','suggestion','video','audio']
          widgets={
               'std_id':forms.TextInput(attrs={"placeholder":"Student Id","class":"form-control","style":"border-radius: 0.75rem; "}),
               'gender':forms.RadioSelect(),
               'age':forms.NumberInput(attrs={"placeholder":"Age","class":"form-control","style":"border-radius: 0.75rem; "}),
          
          }

class UserRegForm(UserCreationForm):
     class Meta:
          model=User
          fields=['username','password1']          


     
class QuesForm(forms.ModelForm):
     class Meta:
          model=Question
          fields='__all__'
     text=forms.CharField(widget=forms.Textarea(attrs={"Placeholder":"Upload Questions","class":"form-control","style":"border-radius: 0.75rem;padding:15px;width:900px;height:150px; "}) )    


class QuesAnsForm(forms.ModelForm):
     class Meta:
          model=Answer
          fields='__all__'
     # question=forms.CharField(widget=forms.ChoiceField(attrs={"Placeholder":"Upload Questions","class":"form-control","style":"border-radius: 0.75rem;rows:2; "}) )    
     text=forms.CharField(widget=forms.TextInput(attrs={"Placeholder":"Upload Answers","class":"form-control","style":"border-radius: 0.75rem;padding:10px; "}) )    

class SugForm(forms.ModelForm):
     class Meta:
          model=Suggestion
          fields=['suggestion','cat']
          suggestion=forms.CharField(widget=forms.Textarea(attrs={"Placeholder":"Upload Answers","class":"form-control","style":"border-radius: 0.75rem;padding:10px; "}) )    

class SugVideoForm(forms.ModelForm):
     class Meta:
          model=Suggestion
          fields=['video','cat']
          # text=forms.CharField(widget=forms.Textarea(attrs={"Placeholder":"Upload Answers","class":"form-control","style":"border-radius: 0.75rem;padding:10px; "}) )    

class SugAudioForm(forms.ModelForm):
     class Meta:
          model=Suggestion
          fields=['audio','cat']
          audio=forms.FileField(widget=forms.FileInput(attrs={"type":"file","name":"audio_file","class":"custom-file-input"}))
          # text=forms.CharField(widget=forms.Textarea(attrs={"Placeholder":"Upload Answers","class":"form-control","style":"border-radius: 0.75rem;padding:10px; "}) )    

class SuggestionForm(forms.ModelForm):
     class Meta:
          model=Suggestion
          fields=['suggestion','video','audio']
     suggestion=forms.CharField(widget=forms.Textarea(attrs={"Placeholder":"Upload Answers","class":"form-control","style":"border-radius: 0.75rem;padding:10px;cols:10; "}) )    
