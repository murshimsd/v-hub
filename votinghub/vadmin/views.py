from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'vadmin/home.html')

def master(request):
    return render(request,'vadmin/master.html')

def add_college(request):
    return render(request,'vadmin/add_college.html')

def view_college(request):
    return render(request,'vadmin/view_college.html')

def master1(request):
    return render(request,'vadmin/master1.html')