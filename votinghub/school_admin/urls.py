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
    path('check_mail_candidate',views.check_mail_candidate,name='check_mail_candidate'),
    path('remove_voter/<int:vid>',views.remove_voter,name='remove_voter'),
    path('remove_candidate/<int:ca_id>',views.remove_candidate,name='remove_candidate'),
    path('remove_position/<int:pid>',views.remove_position,name='remove_position'),
    path('validate_position',views.validate_position,name='validate_position'),
    path('get_positions',views.get_positions,name='get_positions'),
    path('update_password/<int:voter_id>',views.update_password,name='update_password'),
    path('update_candidate/<int:c_id>',views.update_candidate,name='update_candidate'),
    path('update_postion/<int:po_id>',views.update_postion,name='update_position'),
    path('search_voters',views.search_voters,name='search_voters'),
    path('search_position',views.search_position,name='search_position'),
    path('your_view',views.your_view,name='your_view'),
    path('logout',views.logout,name='logout'),
    path('search_candidates',views.search_candidates,name='search_candidates')
    
]