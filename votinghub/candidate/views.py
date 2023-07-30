from django.shortcuts import render , redirect
from .models import Candidates

# Create your views here.
def master_pages(request):
    return render(request,'candidate/master_pages.html')

def profile(request):
    candidat = Candidates.objects.get(id=request.session['candidate'])
    return render(request,'candidate/profile.html',{"candidate":candidat})



def home(request):
    candidat = Candidates.objects.get(id=request.session['candidate'])
    if request.method == 'POST':
        platform_text = request.POST.get('platform', '')
        candidat.platform = platform_text
        candidat.save()
        return redirect('candidate:home')
    return render(request,'candidate/home.html',{"candidate":candidat})



def update_profile(request):
    return render(request,'candidate/update_profile.html')


def logout(request) :
    del request.session['candidate']
    request.session.flush()
    return redirect('common:home')