from django.forms import ModelForm, DateInput
from django.core.exceptions import ValidationError
from app_forms.models import AcademicFormation


class AcademicFormationForm(ModelForm):
    class Meta:
        model = AcademicFormation
        fields = ['institution', 'course', 'start_date',
                  'end_date', 'additional_formations']
        labels = {
            'institution': 'Instiuição ',
            'course': 'Curso ',
            'start_date': 'Data de início',
            'end_date': ' Data de término ',
            'additional_formations': 'Informações adicionais'
        }
        widgets = {
            'start_date': DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'}),
            'end_date': DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'})
        }
