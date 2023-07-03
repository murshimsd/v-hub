from django.shortcuts import render , redirect

from school_admin.views import candidates
from .models import Voter
from django.contrib import messages
from school_admin.models import Positions
from candidate.models import Candidates , Votes


def vote(request):
    voter = Voter.objects.get(id=request.session.get('voter'))
    positions = Positions.objects.filter(title_id=voter.title_id)
    candidates = Candidates.objects.all()

    
    if Votes.objects.filter(voter_id=voter.id).exists():
        return redirect('voter:thanks')

    if request.method == 'POST':
        voter_id = request.session.get('voter')
        for position in positions:
            try:
                candidate_id = request.POST[position.position]
                if not candidate_id:
                    raise Exception("You have skipped a position.")

                voting = Votes(
                    voter_id=voter_id,
                    candidate_id=candidate_id,
                    position_id=position.id
                )
                voting.save()
            except Exception as e:
                messages.error(request, str("skipped"))
                return redirect('voter:vote')
        return redirect('voter:thanks')

    position_candidates = {}
    for position in positions:
        candidates = Candidates.objects.filter(position=position, title_id=voter.title_id)
        position_candidates[position] = candidates

    return render(request, 'voter/vote.html', {"position_candidates": position_candidates})



# def vote(request):
#     voter = Voter.objects.get(id=request.session.get('voter'))
#     positions = Positions.objects.filter(title_id=voter.title_id)
#     candidates = Candidates.objects.all()

#     if request.method == 'POST':
#         voter_id = request.session.get('voter')
#         for position in positions:
#             try:
#                 candidate_id = request.POST[position.position]
#                 if not candidate_id:
#                     raise Exception("You have skipped a position.")

#                 voting = Votes(
#                     voter_id=voter_id,
#                     candidate_id=candidate_id,
#                     position_id=position.id
#                 )
#                 voting.save()
#             except Exception as e:
#                 messages.error(request, str("you have skipped position "))
#                 return redirect('voter:vote')

#         # Redirect the user to the success page after successful voting
#         return redirect('voter:thanks')

#     position_candidates = {}
#     for position in positions:
#         candidates = Candidates.objects.filter(position=position, title_id=voter.title_id)
#         position_candidates[position] = candidates

#     return render(request, 'voter/vote.html', {"position_candidates": position_candidates})




def master(request):
    return render(request,'voter/master.html')




def thanks(request):
    return render(request,'voter/thanks.html')



def profile(request):
    voter = Voter.objects.get(id=request.session['voter'])

    return render(request,'voter/profile.html',{"voter":voter})



def view_vote(request):
    return render(request,'voter/view_vote.html')



def update_profile(request):
    voter = Voter.objects.get(id=request.session['voter'])

    msg = ''
    if request.method == 'POST':
        
        new_fname = request.POST['f_name']
        new_lname = request.POST['l_name']
        new_email = request.POST['email']

        voter.f_name = new_fname
        voter.l_name = new_lname
        voter.e_mail = new_email
        
        
        
       
        voter.save()
        msg = 'successfully updated'
    return render(request,'voter/update_profile.html',{"voter":voter,"msg":msg})







def logout(request) :
    del request.session['voter']
    request.session.flush()
    return redirect('common:home')