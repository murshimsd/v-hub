from django.urls import path
from . import views

app_name='voter' # for redirection purpose

urlpatterns=[

    path('vote',views.vote,name='vote'),
    path('master',views.master,name='master'),
    path('view_vote',views.view_vote,name='view_vote'),
    path('profile',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'), 
    path('logout',views.logout,name='logout'),

    
    path('thanks',views.thanks,name='thanks'),
    




]
