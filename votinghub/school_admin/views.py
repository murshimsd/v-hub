from django.shortcuts import render

# Create your views here.

def master(request):
    return render(request,'school_admin/master.html')

def home(request):
    return render(request,'school_admin/home.html')

def voters(request):
    return render(request,'school_admin/voters.html')

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




