from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=100, blank= True)
    author=models.CharField(max_length=100, blank= True)
    isbn=models.CharField(max_length=100, blank= True)
    publisher=models.CharField(max_length=100, blank= True)
    def _str_(self):
        return self.title