from django.urls import path
from .views import *

urlpatterns =[
    path('shome/',StuHomeView.as_view(),name="sh"),
    path('ex/',studentanswer,name='ans'),
    path('submit/',submit_exam,name='submit_exam'),
    path('profile/',Profile.as_view(),name='pro'),
    path('sug/',SugView.as_view(),name='sug'),
    path('result/',ResultView.as_view(),name='res'),
    path('cp/',ChangePasswordView.as_view(),name="cp"),
    path('logout/',LogOut.as_view(),name="logout"),

]