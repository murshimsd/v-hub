from django.urls import path
from . import views

app_name='school_admin' # for redirection purpose

urlpatterns = [

    path('master',views.master,name='master'),
    path('home',views.home,name='home'),
    path('voters',views.voters,name='voters'),
    path('positions',views.positions,name='positions'),
    path('title',views.title,name='title'),
    path('candidates',views.candidates,name='candidates'),
    path('ballot_position',views.ballot_position,name='ballot_position'),
    path('votes',views.votes,name='votes'),
    path('check_mail',views.check_mail,name='check_mail'),
    path('remove_voter/<int:vid>',views.remove_voter,name='remove_voter'),
    path('update_voter/<int:v_id>',views.update_voter,name='update_voter')

]