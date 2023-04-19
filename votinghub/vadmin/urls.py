from django.urls import path
from . import views

app_name='vadmin' # for redirection purpose

urlpatterns=[

    path('home',views.home,name='home'),
    path('master',views.master,name='master'),
    path('add_college',views.add_college,name='add_college'),
    path('view_college',views.view_college,name='view_college')
    
]