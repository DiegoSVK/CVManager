from django.db import models
from cv_platform.models import Resume



class Contact(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    cep =models.CharField(max_length=10)
    state = models.CharField(max_length=50)
    city =models.CharField(max_length=50)
    address = models.CharField(max_length=100)

def __str__(self):
    return f'{self.email}'