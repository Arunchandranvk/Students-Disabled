from django.urls import path
from .views import *

urlpatterns = [
    path('mainhome/',HomeView.as_view(),name='h'),
    path('students/',StudentsView.as_view(),name='stu'),
    path('search/',Search.as_view(),name="sea"),
    path('detail/<int:pk>/',DetailView.as_view(),name='det'),
    path('Test_details/',Score_view.as_view(),name='score'),
    path('qhome/',Ques.as_view(),name="q")
]