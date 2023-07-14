from django.http import JsonResponse
from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.contrib import messages
from voter.models import Voter 
from candidate.models import Candidates , Votes
from .models import Title , Positions
from django.db.models import F,Q
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.db.models import Count, F, Max


import random
from django.conf import settings



# Create your views here.

def master(request):
    return render(request,'school_admin/master.html')


# def result(request):
#     positions = Positions.objects.filter(title_id=2)

#     results1=[]
#     results = []
#     result_array=[]
#     for position in positions:
#         candidates = Candidates.objects.filter(position_id=position.id)
#         candidate_results = Votes.objects.filter(position_id=position.id).values('candidate').annotate(vote_count=Count('candidate')).order_by('-vote_count')
        

        
#         for candidate_result in candidate_results:
#             candidate = Candidates.objects.get(pk=candidate_result['candidate'])
#             vote_count = candidate_result['vote_count']
#             result_array.append({'candidate': candidate, 'vote_count': vote_count})



#         winner = candidate_results.first() if candidate_results else None
#         results.append({'position': position, 'candidates': candidates, 'candidate_results': candidate_results, 'winner': winner})
    
#     return render(request, 'school_admin/result.html', {'results': results})

def result(request):
    # Retrieve all positions for the election
    aaa = Title.objects.get(status='active')
    positions = Positions.objects.filter(title_id=aaa.id)

    # Prepare the results data for each position
    results = []
    for position in positions:
        candidates = Candidates.objects.filter(position_id=position.id)
        candidate_results = (
            Votes.objects.filter(position_id=position.id)
            .values('candidate', 'candidate__name')  # Include candidate's name
            .annotate(vote_count=Count('candidate'))
            .order_by('-vote_count')
        )

        winner = candidate_results.first() if candidate_results else None
        print(winner)
        results.append({'position': position, 'candidates': candidates, 'candidate_results': candidate_results, 'winner': winner})
        # print(results)


    return render(request, 'school_admin/result.html', {'results': results,"title_name":aaa})
  




def logout(request) :
    del request.session['admins']
    request.session.flush()
    return redirect('common:home')




def home(request):
    titles= Title.objects.get(status='active')
    voters_count = Voter.objects.filter(title_id=titles.id).count()
    candidates_count = Candidates.objects.filter(title_id=titles.id).count()
    positions_count = Positions.objects.filter(title_id=titles.id).count()
    return render(request,'school_admin/home.html',{"voters_count":voters_count,"candidates_count":candidates_count,"positions_count":positions_count})




def voters(request):
    titles = Title.objects.get(status='active')
    
    msg = ''
    voters = Voter.objects.filter(title_id=titles.id)
    if request.method == 'POST':
        vf_name = request.POST['f_name']
        vl_name = request.POST['l_name']
        v_photo = request.FILES["photo"]
        v_email = request.POST['emails']
        v_password = random.randint(1111,9999)
        v_title = request.POST['title']

        voter_exist = Voter.objects.filter(e_mail = v_email,title_id=v_title).exists()
        if not voter_exist :
            new_voter = Voter (
                f_name = vf_name,
                l_name = vl_name,
                photo = v_photo,
                e_mail = v_email,
                password = v_password,
                title_id = v_title
                
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
            msg = 'mail exist'

    

    return render(request,'school_admin/voters.html',{"msg":msg,"voters":voters,"titles":titles})





def positions(request):

    titles = Title.objects.get(status='active')
    positions = Positions.objects.filter(title_id=titles.id)




    msg = ''
    if request.method == 'POST':
        vf_position = request.POST['position']
        vl_title = request.POST['title']
        v_votes = request.POST["no_votes"]
        position_exist = Positions.objects.filter(position=vf_position,title_id=vl_title).exists()
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
    msg = ''
    
    if request.method == 'POST':
        vf_name = request.POST['name']
        vl_date = request.POST['date']
        

        title_exist = Title.objects.filter(title = vf_name).exists()
        if not title_exist :
            new_title = Title (
                title = vf_name,
                date = vl_date,
                
                
            )
            
            new_title.save()
            msg = 'success'
            

        else :
            msg = 'election already  exist '
    return render(request,'school_admin/title.html',{"titles":title,"msg":msg})






def candidates(request):
    titles = Title.objects.get(status='active')
    candidatess = Candidates.objects.filter(title_id=titles.id)


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
        candidate_exist = Candidates.objects.filter(email=c_mail,title_id=titles.id).exists()
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

    return render(request,'school_admin/candidates.html',{"titles":titles,"msg":msg,"candidates":candidatess})





def get_positions(request):
    title_id = request.GET.get('title_id')
    # Fetch the positions based on the selected title ID
    positions = Positions.objects.filter(title_id=title_id).values('id', 'position')

    return JsonResponse({'positions': list(positions)})





def ballot_position(request):
    titles= Title.objects.get(status='active')
    positions = Positions.objects.filter(title_id=titles.id)

    position_candidates = {}
    for position in positions:
        candidates = Candidates.objects.filter(position=position)
        position_candidates[position] = candidates
    return render(request,'school_admin/ballot_position.html',{'position_candidates': position_candidates})







def votes(request):
    votess = Title.objects.get(status='active')
    votess_id = Votes.objects.filter(title_id=votess.id)

    return render(request,'school_admin/votes.html',{"votes":votess_id,'id':votess})






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
    titles = request.POST['id']
    exist = Voter.objects.filter(e_mail=email_ajax,title_id=titles).exists()
    return JsonResponse({"email_exist":exist})





def check_mail_candidate(request):
    email_ajax = request.POST['candidateEmail'] 
    titles = request.POST['id']
    exist = Candidates.objects.filter(email=email_ajax,title_id=titles).exists()
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
    title_id = request.GET.get('id')
    voters = Voter.objects.filter(f_name__icontains=search_query ,title_id=title_id)
    
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




def search_votes(request):
    query = request.GET.get('search')
    title_id = request.GET.get('id')
    print(title_id)
    results = Votes.objects.filter(voter__f_name__icontains=query,title_id=title_id)
    
    data = []
    for vote in results:
        data.append({
            'position': vote.position.position,
            'candidate': vote.candidate.name,
            'voter': vote.voter.f_name,
        })
    
    return JsonResponse(data, safe=False)









def search_position(request):
    search_word = request.GET.get('search')
    title_id = request.GET.get('id')
    print(title_id)

    # Filter positions based on the search word
    positions = Positions.objects.filter(title_id=title_id,position__icontains=search_word)

    # Convert positions queryset to a list of dictionaries
    positions_data = [
        {
            'position': position.position,
            'title': position.title.title,  # Access the title attribute of the related model
            'no_votes': position.no_votes,
            'id' : position.id
            
        }
        for position in positions
    ]

    # Return the filtered positions as JSON data
    return JsonResponse(positions_data, safe=False)






def search_candidates(request):
    search_word1 = request.GET.get('search')
    title_ids = request.GET.get('id')
    candidatesss = Candidates.objects.filter(name__icontains=search_word1,title_id=title_ids)
    results = []
    # results=[{'search':search_word1,'id':title_ids}]

    for candidate in candidatesss:
        result = {
            'name': candidate.name,
            'photo_url': candidate.photo.url,
            'position': candidate.position.position,
            'password': candidate.password,
            'email':candidate.email,
            'id': candidate.id
            # Add other fields as needed
        }
        results.append(result)

    return JsonResponse(results, safe=False)





# def search_voters(request):
#     search_query = request.GET.get('search')
#     title_id = request.GET.get('id')
#     voters = Voter.objects.filter(f_name__icontains=search_query ,title_id=title_id)
    
#     results = []

#     for voter in voters:
#         result = {
#             'f_name': voter.f_name,
#             'l_name': voter.l_name,
#             'photo_url': voter.photo.url,
#             'password': voter.password,
#             'id': voter.id
#             # Add other fields as needed
#         }
#         results.append(result)

#     return JsonResponse(results, safe=False)







def your_views(request):
    titles = Title.objects.all()  # Replace `Title` with your actual model name
    active_title = Title.objects.filter(status='active').first()
    active_index = titles.index(active_title) if active_title else None

    context = {
        'titles': titles,
        'activeIndex': active_index,
    }
    return render(request, 'school_admin/title.html', context)



def update_status(request):
    if request.method == 'POST':
        index = int(request.POST.get('index'))
        items = Title.objects.all()

        if 0 <= index < len(items):
            selected_item = items[index]

            # Set all items to 'non-active'
            Title.objects.exclude(pk=selected_item.pk).update(status='non-active')

            # Set the selected item to 'active'
            selected_item.status = 'active'
            selected_item.save()

            return JsonResponse({'message': 'Status updated successfully.'})

    return JsonResponse({'message': 'Invalid request.'}, status=400)





def election_results(request):
    positions = Positions.objects.filter(title_id=2)

    
    results = []
    for position in positions:
        candidates = Candidates.objects.filter(position_id=position.id)
        candidate_results = Votes.objects.filter(position_id=position.id).values('candidate').annotate(vote_count=Count('candidate')).order_by('-vote_count')
        winner = candidate_results.first() if candidate_results else None
        results.append({'position': position, 'candidates': candidates, 'candidate_results': candidate_results, 'winner': winner})
    print(results,'lll')
    return render(request, 'school_admin/result.html', {'results': results})
