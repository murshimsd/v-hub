from django.urls import path
from . import views

app_name='candidate' # for redirection purpose

urlpatterns=[


    path('master_pages',views.master_pages,name='master_pages'),
    path('profile',views.profile,name='profile'),
    path('update_profile',views.update_profile,name='update_profile'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout')




]