
from django.db import models
from cv_platform.models import Resume


class AcademicFormation(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    additional_formations = models.TextField(null=True, blank=True)

def __str__(self):
    return f'{self.institution} - {self.course}'
