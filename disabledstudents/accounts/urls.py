from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('addd/',AddStudent.as_view(),name='add'),
    path('quest/<int:pk>/',QuestView.as_view(),name='que'),
    path('questall/',QuestViewAll.as_view(),name='ques'),
    path('test/<int:pk>/',Test,name='tt'),
    path('assign/',AssignView,name='testall'),
    # path('get_suggestions/', views.get_suggestions, name='get_suggestions'),   
]