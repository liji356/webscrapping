from django.db import models

class Links(models.Model):
    address=models.CharField(max_length=500,null=True,blank=True)
    stringname=models.CharField(max_length=500,null=True,blank=True)


    def __str__(self):
        return self.stringname
# Create your models here.
