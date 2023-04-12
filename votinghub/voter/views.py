from django.shortcuts import render



def vote(request):
    return render(request,'voter/vote.html')

def master(request):
    return render(request,'voter/master.html')

def profile(request):
    return render(request,'voter/profile.html')

def view_vote(request):
    return render(request,'voter/view_vote.html')