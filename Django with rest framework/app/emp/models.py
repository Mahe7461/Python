from django.db import models

# Create your models here.
class Empolyeeclass(models.Model):
   # Name1 = models.CharField(max_length=20)
    #Email = models.CharField(max_length=30)
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=8)
    department=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    