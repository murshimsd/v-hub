from django.db import models

# Create your models here.


class Admin (models.Model) :
    user_id = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


    class Meta :
        db_table = 'admin_tb'


class Title(models.Model):
    title = models.CharField(max_length=500)

    class Meta :
        db_table = 'title_tb'

class Positions(models.Model):
    position = models.CharField(max_length=50)
    no_votes = models.BigIntegerField()
    title = models.ForeignKey(Title,on_delete=models.CASCADE)
    

    class Meta :
        db_table = 'positions_tb'




