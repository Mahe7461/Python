from django.db import models

# Create your models here.
class students(models.Model):
    Stu_Name= models.CharField(max_length=50)
    Roll_no= models.IntegerField
    def __str__(self):
        return self.Stu_Name
    def get_queryset(self):
        User=self.request.user
        return User.accounts.all()

