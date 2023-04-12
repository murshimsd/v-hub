from django.urls import path
from . import views

app_name='common' # for redirection purpose

urlpatterns=[


    path('voter_login',views.voter_login,name='voter_login'),
    path('',views.home,name='home'),
    path('master',views.master,name='master'),
    path('candidate_login',views.candidate_login,name='candidate_login'),
    path('about',views.about,name='about'),
    path('contacts',views.contacts,name='contacts'),
    path('admin_login',views.admin_login,name='admin_login'),



]