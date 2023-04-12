from django.urls import path
from . import views

app_name='school_admin' # for redirection purpose

urlpatterns = [

    path('master',views.master,name='master'),
    path('home',views.home,name='home'),
     path('master1',views.master1,name='master1'),

]