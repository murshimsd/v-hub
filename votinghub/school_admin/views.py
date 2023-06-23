from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.contrib import messages
from voter.models import Voter
from candidate.models import Candidates
from .models import Title , Positions

import random
from django.conf import settings


# Create your views here.

def master(request):
    return render(request,'school_admin/master.html')




def logout(request) :
    del request.session['admins']
    request.session.flush()
    return redirect('common:home')




def home(request):
    voters_count = Voter.objects.all().count()
    candidates_count = Candidates.objects.all().count()
    positions_count = Positions.objects.all().count()
    return render(request,'school_admin/home.html',{"voters_count":voters_count,"candidates_count":candidates_count,"positions_count":positions_count})




def voters(request):
    msg = ''
    voters = Voter.objects.all()
    if request.method == 'POST':
        vf_name = request.POST['f_name']
        vl_name = request.POST['l_name']
        v_photo = request.FILES["photo"]
        v_email = request.POST['emails']
        v_password = random.randint(1111,9999)

        voter_exist = Voter.objects.filter(e_mail = v_email).exists()
        if not voter_exist :
            new_voter = Voter (
                f_name = vf_name,
                l_name = vl_name,
                photo = v_photo,
                e_mail = v_email,
                password = v_password,
                
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

    titles = Title.objects.all()
    positions = Positions.objects.all()




    msg = ''
    if request.method == 'POST':
        vf_position = request.POST['position']
        vl_title = request.POST['title']
        v_votes = request.POST["no_votes"]
        position_exist = Positions.objects.filter(position=vf_position,title=vl_title).exists()
        if not position_exist :
            new_position = Positions (

                position = vf_position,
                no_votes = v_votes,
                title_id = vl_title

            )
            new_position.save()
            msg = 'success'
        else :
            msg = 'already exist'
            

    return render(request,'school_admin/positions.html',{"msg":msg,"titles":titles,"positions":positions})






def validate_position(request):
    if request.method == 'GET':
        position = request.GET.get('position')
        title_id = request.GET.get('title_id')

        try:
            Positions.objects.get(position=position, title_id=title_id)
            data = {'valid': False, 'message': 'Position already exists for this election'}
        except Positions.DoesNotExist:
            data = {'valid': True}

        return JsonResponse(data)
    


    
    

def title(request):
    title = Title.objects.all()
    return render(request,'school_admin/title.html',{"titles":title})






def candidates(request):
    titles = Title.objects.all()
    candidatess = Candidates.objects.all()


    msg = ''
    if request.method == 'POST':
        print(request.POST)  # Check the request.POST dictionary in the console
        c_title_id = request.POST['title']
        c_position_id = request.POST['position']
        c_name = request.POST['name']
        c_mail = request.POST['email']
        c_title = request.POST['title']
        c_position = request.POST['position']
        c_platform = request.POST['platform']
        c_photo = request.FILES['photo']
        c_password = random.randint(1111,9999)
        candidate_exist = Candidates.objects.filter(email=c_mail).exists()
        if not candidate_exist :
            title = Title.objects.get(id=c_title_id)
            position = Positions.objects.get(id=c_position_id)
            new_candidates = Candidates(
                name = c_name,
                email = c_mail,
                password = c_password,
                photo = c_photo,
                platform = c_platform,
                title_id = c_title,
                position_id = c_position

            )
            pas = 'your approved as a candidate your password is '+str(c_password)
            new_candidates.save()
            msg = 'success'
            send_mail(
                'v_hub password',
                pas,
                settings.EMAIL_HOST_USER,
                [new_candidates.email]

            )

        else :
            msg = 'already existed mail'

    return render(request,'school_admin/candidates.html',{"titles":titles,"msgs":msg,"candidates":candidatess})





def get_positions(request):
    title_id = request.GET.get('title_id')
    # Fetch the positions based on the selected title ID
    positions = Positions.objects.filter(title_id=title_id).values('id', 'position')

    return JsonResponse({'positions': list(positions)})





def ballot_position(request):
    positions = Positions.objects.all()

    position_candidates = {}
    for position in positions:
        candidates = Candidates.objects.filter(position=position)
        position_candidates[position] = candidates
    return render(request,'school_admin/ballot_position.html',{'position_candidates': position_candidates})







def votes(request):
    return render(request,'school_admin/votes.html')






def remove_voter(request,vid) :
    voter= Voter.objects.get(id=vid)
    voter.delete()
    return redirect("school_admin:voters")



def remove_candidate(request,ca_id) :
    candidate= Candidates.objects.get(id=ca_id)
    candidate.delete()
    return redirect("school_admin:candidates")



def remove_position(request,pid) :
    position= Positions.objects.get(id=pid)
    position.delete()
    return redirect("school_admin:positions")





def check_mail(request):
    email_ajax = request.POST['voterEmail'] #recieved from ajax
    exist = Voter.objects.filter(e_mail=email_ajax).exists()
    return JsonResponse({"email_exist":exist})





def check_mail_candidate(request):
    email_ajax = request.POST['candidateEmail'] #recieved from ajax
    exist = Candidates.objects.filter(email=email_ajax).exists()
    return JsonResponse({"email_exist":exist})





def update_password(request, voter_id):
 
    msg = ''
    if request.method == 'POST':
        new_password = request.POST['passwrds']
        n_mail = request.POST['e1']
       
        voter = Voter.objects.get(id=voter_id)
        voter.password = new_password
        voter.save()
        msg='your new voting password is'+str(new_password)
        send_mail(
                'v_hub password',
                msg,
                settings.EMAIL_HOST_USER,
                [n_mail]

            )
        
        return redirect('school_admin:voters')
    




def update_candidate(request, c_id):
 
    msg = ''
    if request.method == 'POST':
        new_password = request.POST['passwrds']
        n_mail = request.POST['e2']
       
        candidates = Candidates.objects.get(id=c_id)
        candidates.password = new_password
        candidates.save()
        msg='your new updated candidate password is'+str(new_password)
        send_mail(
                'v_hub password',
                msg,
                settings.EMAIL_HOST_USER,
                [n_mail]

            )
        
        return redirect('school_admin:candidates')
    






def update_postion(request, po_id):
 
    msg = ''
    if request.method == 'POST':
        
        n_votes = request.POST['number']
       
        position = Positions.objects.get(id=po_id)
        position.no_votes = n_votes
        position.save()
        return redirect('school_admin:positions')
    



    
    





def your_view(request):
    
    voters = Voter.objects.all()
    return render(request, 'school_admin/voters.html', {'voters': voters})






def search_voters(request):
    search_query = request.GET.get('search')
    voters = Voter.objects.filter(f_name__icontains=search_query)
    results = []

    for voter in voters:
        result = {
            'f_name': voter.f_name,
            'l_name': voter.l_name,
            'photo_url': voter.photo.url,
            'password': voter.password,
            'id': voter.id
            # Add other fields as needed
        }
        results.append(result)

    return JsonResponse(results, safe=False)



