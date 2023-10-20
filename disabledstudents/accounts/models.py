from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class Subjects(models.Model):
   name=models.CharField(max_length=100)

   class Meta:
       ordering=('name',)
       verbose_name_plural="Subject"

   def __str__(self):
        return self.name



class Student(models.Model):
    std_id=models.CharField(unique=True,max_length=50)
    first_name=models.CharField(max_length=100,null=True,blank=True)
    last_name=models.CharField(max_length=100,null=True,blank=True)
    img=models.FileField(upload_to="student image",null=True,blank=True)
    options=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others")
    )
    gender=models.CharField(max_length=100,choices=options,default="Male")
    age=models.PositiveIntegerField(null=True)
    d_type=(
        ("Mobility Impairment","Mobility Impairment"),
        ("Visual Impairment","Visual Impairment"),
        ("Hearing Impairment","Hearing Impairment"),
        ("Learning Disability","Learning Disability"),
        ("Autism Spectrum Disorder","Autism Spectrum Disorder"),
        ("Speech Impairment","Speech Impairment"),
        ("Intellectual Disability","Intellectual Disability"),
    )
    disability=models.CharField(max_length=100,choices=d_type,default="Mobility Impairment")
    a_techno=(
        ("Screen Reader","Screen Reader"),
        ("Communication App","Communication App"),
        ("Hearing Aids","Hearing Aid"),
        ("Voice Recognition","Voice Recognition"),
        ("Wheelchair","Wheelchair"),
        ("Assistive Learning Tools","Assistive Learning Tools"),
        ("Text-to-Speech Software","Text-to-Speech Software"),
        ("Augmentative and Alternative Communication (AAC) Device","Augmentative and Alternative Communication (AAC) Device"),
    )
    accesstechnology=models.CharField(max_length=200,choices=a_techno,default="Screen Reader")
    score = models.IntegerField(null=True)
    category = models.CharField(max_length=200,null=True)
    suggestion=models.TextField(null=True) 
    video=models.FileField(upload_to='suggested video',null=True)
    audio=models.FileField(upload_to='suggested audio',null=True)

    def __str__(self):
        return self.std_id
    
class CustUser(AbstractUser):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='cust',null=True)
    

class Question(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,default="question")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.student} - {self.question}" 

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name   
    
class Suggestion(models.Model):
     suggestion=models.TextField(null=True)  
     cat=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='sugg')  
     video=models.FileField(upload_to='suggested video',null=True)
     audio=models.FileField(upload_to='suggested audio',null=True)
     thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
     
     def __str__(self):
        return self.cat.name
     
# class Assignment(models.Model): 
#     student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='stu_ag')
#     test=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='tes_ag')     




 


