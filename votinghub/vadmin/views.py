from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import random
from.models import Schools

# Create your views here.

def home(request):
    return render(request,'vadmin/home.html')

def master(request):
    return render(request,'vadmin/master.html')

def add_college(request):
    msg = ''
    if request.method == 'POST':
        s_name = request.POST['school_name']
        s_user_name = request.POST['user_name']
        s_email = request.POST['email']
        s_city = request.POST['city']
        s_state = request.POST['state']
        s_password = random.randint(1111,9999)

        school_exist = Schools.objects.filter(e_mail = s_email).exists()
        if not school_exist :
            new_school = Schools(
                college_name = s_name,
                user_name = s_user_name,
                city = s_city,
                state = s_state,
                e_mail = s_email,
                password = s_password
                


            )
            new_school.save()
            pas = 'your password is '+str(s_password)
            
            msg = 'success'
            send_mail(
                'v_hub password',
                pas,
                settings.EMAIL_HOST_USER,
                [new_school.e_mail]

            )


        else :
            msg = 'mail already exist'





    return render(request,'vadmin/add_college.html',{"msg":msg})

def view_college(request):
    school = Schools.objects.all()
    return render(request,'vadmin/view_college.html',{"schools":school})


def check_mail(request):
    email_ajax = request.POST['schoolEmail'] #recieved from ajax
    exist = Schools.objects.filter(e_mail=email_ajax).exists()
    return JsonResponse({"email_exist":exist})



