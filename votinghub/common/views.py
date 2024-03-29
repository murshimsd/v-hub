from django.shortcuts import render , redirect
from voter.models import Voter
from candidate.models import Candidates
from school_admin.models import Admin
# from vadmin.models import Schools

# Create your views here.

def vote(request):
    return render(request,'common/vote.html')
 
def admin_login(request):
    msg = ''
    if request.method == 'POST':
        u_name = request.POST['user_id']
        passwords = request.POST['password']

        try:
            admins = Admin.objects.get(user_id = u_name,password=passwords)
            request.session['admins'] = admins.id
            msg = 'correct'
            return redirect('school_admin:home')
        except:
            msg = 'incorrect'

    return render(request,'common/admin_login.html',{"msg":msg})
    




def voter_login(request):
    msgs = ''

    if request.method == 'POST':

        v_email = request.POST['email']
        passwords = request.POST['password']

        try:
            voter = Voter.objects.get(e_mail = v_email , password = passwords )
            request.session['voter'] = voter.id
            request.session['voter_name'] = voter.f_name
            request.session['voter_photo'] = voter.photo.url
            return redirect('voter:vote')

        except :
            msgs = 'incorrect mail or password'


    return render(request,'common/voter_login.html',{"msg":msgs})   







def candidate_login(request):

    msgs = ''

    if request.method == 'POST':

        v_email = request.POST['email']
        passwords = request.POST['password']
        print(passwords+'fghjjjjjjjkkk')

        try:
            candidate = Candidates.objects.get(email = v_email , password = passwords )
            request.session['candidate'] = candidate.id
            request.session['candidate_name'] = candidate.name
            request.session['candidate_photo'] = candidate.photo.url
            return redirect('candidate:home')

        except :
            msgs = 'incorrect mail or password'

    return render(request,'common/candidate_login.html',{"msg":msgs})  




def voter_register(request):
    return render(request,'common/voter_register.html')   

def home(request):
    
    return render(request,'common/home.html') 

def master(request):
    return render(request,'common/master.html')    
 

def about(request):
    return render(request,'common/about.html')  

def contacts(request):
    return render(request,'common/contacts.html')       