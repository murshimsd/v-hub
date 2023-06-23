from django.db import models
from school_admin.models import Title , Positions




class Candidates(models.Model):
    name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 30)
    photo = models.ImageField(upload_to = 'candidate/')
    email = models.CharField(max_length=50)
    title = models.ForeignKey(Title,on_delete=models.CASCADE)
    position = models.ForeignKey(Positions,on_delete=models.CASCADE)
    platform = models.CharField(max_length=100,default='')


    class Meta:
        db_table = 'candidate_tb'


















    


    