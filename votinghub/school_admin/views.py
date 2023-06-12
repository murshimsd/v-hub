from django.shortcuts import render , redirect
from django.core.mail import send_mail
from voter.models import Voter
import random
from django.conf import settings


# Create your views here.

def master(request):
    return render(request,'school_admin/master.html')

def home(request):
    return render(request,'school_admin/home.html')

def voters(request):
    msg = ''
    voters = Voter.objects.all()
    if request.method == 'POST':
        vf_name = request.POST['f_name']
        vl_name = request.POST['l_name']
        v_photo = request.FILES['photo']
        v_email = request.POST['emails']
        v_password = random.randint(1111,9999)

        voter_exist = Voter.objects.filter(e_mail = v_email).exists()
        if not voter_exist :
            new_voter = Voter (
                f_name = vf_name,
                l_name = vl_name,
                photo = v_photo,
                e_mail = v_email,
                password = v_password
            )
            pas = 'your password is '+str(v_password)
            new_voter.save()
            msg = 'success'
            send_mail(
                'v_hub password',
                pas,
                settings.EMAIL_HOST_USER,
                [new_voter.e_mail]

            )

            

        else :
            msg = 'mail exist '

    

    return render(request,'school_admin/voters.html',{"msg":msg,"voters":voters})

def positions(request):
    return render(request,'school_admin/positions.html')

def title(request):
    return render(request,'school_admin/title.html')

def candidates(request):
    return render(request,'school_admin/candidates.html')

def ballot_position(request):
    return render(request,'school_admin/ballot_position.html')

def votes(request):
    return render(request,'school_admin/votes.html')


def remove_voter(request,vid) :
    voter= Voter.objects.get(id=vid)
    voter.delete()
    return redirect("school_admin:voters")




