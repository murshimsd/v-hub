from django.shortcuts import render , redirect

from school_admin.views import candidates
from .models import Voter
from django.contrib import messages
from school_admin.models import Positions , Title
from candidate.models import Candidates , Votes
from django.db.models import Count


def vote(request):
    titles=Title.objects.get(status='active')
    title_ids = Title.objects.get(id=titles.id)
    voter = Voter.objects.get(id=request.session.get('voter'))
    positions = Positions.objects.filter(title_id=voter.title_id)
    candidates = Candidates.objects.all()

    
    if Votes.objects.filter(voter_id=voter.id).exists():
        return redirect('voter:thanks')

    if request.method == 'POST':
        voter_id = request.session.get('voter')
        has_selection = False  # Variable to check if at least one candidate is selected

        for position in positions:
            try:
                candidate_id = request.POST.get(position.position)
                if candidate_id:
                    has_selection = True  # Set has_selection to True if a candidate is selected
                    voting = Votes(
                        voter_id=voter_id,
                        candidate_id=candidate_id,
                        position_id=position.id,
                        title_id=title_ids.id  # Update this with the appropriate title_id
                    )
                    voting.save()
            except Exception as e:
                messages.error(request, str("skipped"))
                return redirect('voter:vote')

        if has_selection:
            return redirect('voter:thanks')
        else:
            messages.error(request, "You have not selected any candidates.")
            return redirect('voter:vote')

    position_candidates = {}
    for position in positions:
        candidates = Candidates.objects.filter(position=position, title_id=voter.title_id)
        position_candidates[position] = candidates

    return render(request, 'voter/vote.html', {"position_candidates": position_candidates})







def master(request):
    return render(request,'voter/master.html')




def thanks(request):
    return render(request,'voter/thanks.html')



def profile(request):
    voter = Voter.objects.get(id=request.session['voter'])

    return render(request,'voter/profile.html',{"voter":voter})



def view_vote(request):
    voter = Voter.objects.get(id=request.session['voter'])
    try:
        aaa = Title.objects.get(result='published', id=voter.title_id)
        positions = Positions.objects.filter(title_id=aaa.id)
    except Title.DoesNotExist:
        aaa = None
        positions = []

    # Prepare the results data for each position
    results = []
    for position in positions:
        candidates = Candidates.objects.filter(position_id=position.id)
        candidate_results = (
            Votes.objects.filter(position_id=position.id)
            .values('candidate', 'candidate__name')  
            .annotate(vote_count=Count('candidate'))
            .order_by('-vote_count')
        )

        max_vote_count = candidate_results.first()['vote_count'] if candidate_results else 0
        
        # Get all candidates with the maximum vote count as winners
        winners = [candidate for candidate in candidate_results if candidate['vote_count'] == max_vote_count]
        results.append({'position': position, 'candidates': candidates, 'candidate_results': candidate_results, 'winners': winners})
        
    return render(request, 'voter/view_vote.html', {'results': results, 'title_name': aaa})



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



