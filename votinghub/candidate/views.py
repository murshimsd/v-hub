from django.shortcuts import render

# Create your views here.
def master_pages(request):
    return render(request,'candidate/master_pages.html')

def profile(request):
    return render(request,'candidate/profile.html')

def home(request):
    return render(request,'candidate/home.html')



def update_profile(request):
    return render(request,'candidate/update_profile.html')