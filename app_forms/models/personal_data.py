from django.db import models
from cv_platform.models import Resume




class PersonalData(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    birth_date = models.DateField()
    cpf = models.CharField(max_length=14)

    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self) -> str:
        return f'{self.first_name}-{self.last_name}'
