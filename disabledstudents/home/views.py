from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import *
from django.db.models import Q

import pandas as pd
import random
# Create your views here.





class HomeView(TemplateView):
    template_name="home.html"


class StudentsView(TemplateView):
    template_name="students.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data']=Student.objects.all().order_by('std_id')
        return context


class Search(TemplateView):
    template_name="d_search.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query=self.request.GET.get('query')
        if query:
               context["data"]=Student.objects.filter(Q( std_id__icontains=query) )
        # context['search']=Product.objects.get('query')
        return context     
    
class DetailView(TemplateView):
     template_name='detail.html'
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)    
          id=kwargs.get('pk') 
          context['data']=Student.objects.get(id=id)
          return context
     
class Score_view(TemplateView):
     template_name='testscore.html'
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context['data']=StudentAnswer.objects.all().order_by('student')
          context['que']=Question.objects.all()
          query=self.request.GET.get('query')
          if query:              
             context["searchs"]=StudentAnswer.objects.filter(Q( student=query) )
          else :
               None   
          return context
     
     

     