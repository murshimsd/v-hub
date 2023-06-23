from django.db import models

# Create your models here.
class Schools(models.Model):
    college_name = models.CharField(max_length = 50)
    user_name = models.CharField(max_length = 40)
    city = models.CharField(max_length = 40 ,default = '')
    state = models.CharField(max_length=40)
    e_mail = models.CharField(max_length = 30,default='')
    password = models.CharField(max_length=40,default='')


    class Meta:
        db_table = 'school_tb'