from django.shortcuts import render , redirect
from .models import Voter



def vote(request):
    return render(request,'voter/vote.html')

def master(request):
    return render(request,'voter/master.html')

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