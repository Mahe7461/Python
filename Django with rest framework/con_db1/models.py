from django.db import models


    

    
# Create your models here.
class Fulldata(models.Model):
    name= models.CharField(max_length=200)
    def __str__(self):
        return self.name
class data(models.Model):
    fulldata= models.Foreignkey(Fulldata, on_delete=models.CASCADE)
    address= models.CharField(max_length=200)
    

        

                        

