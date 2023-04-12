from django.shortcuts import render

# Create your views here.

def master(request):
    return render(request,'school_admin/master.html')

def home(request):
    return render(request,'school_admin/home.html')

def master1(request):
    return render(request,'school_admin/master1.html')
