from django.shortcuts import render

# Create your views here.

def vote(request):
    return render(request,'common/vote.html')
 
def admin_login(request):
    return render(request,'common/admin_login.html')    

def voter_login(request):
    return render(request,'common/voter_login.html')   

def voter_register(request):
    return render(request,'common/voter_register.html')   

def home(request):
    return render(request,'common/home.html') 

def master(request):
    return render(request,'common/master.html')    

def candidate_login(request):
    return render(request,'common/candidate_login.html')  

def about(request):
    return render(request,'common/about.html')  

def contacts(request):
    return render(request,'common/contacts.html')       