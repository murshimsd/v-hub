from django.db import models
from school_admin.models import Title , Positions
from voter.models import Voter




class Candidates(models.Model):
    name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 30)
    photo = models.ImageField(upload_to = 'candidate/')
    email = models.CharField(max_length=50)
    title = models.ForeignKey(Title,on_delete=models.CASCADE)
    position = models.ForeignKey(Positions,on_delete=models.CASCADE)
    platform = models.CharField(max_length=100,default='',null=True)


    class Meta:
        db_table = 'candidate_tb'





class Votes(models.Model):
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidates, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE,default=0)
    
    
    

    class Meta:
        db_table = 'votes_tb'




















    


    