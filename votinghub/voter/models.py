from django.db import models
from django import forms
# from vadmin.models import Schools

# Create your models here.

class Voter(models.Model):
    f_name = models.CharField(max_length = 30)
    l_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20 ,default = '')
    photo = models.ImageField(upload_to  = 'voter/')
    e_mail = models.CharField(max_length = 30,default='')

    


    class Meta:
        db_table = 'voter_tb'

