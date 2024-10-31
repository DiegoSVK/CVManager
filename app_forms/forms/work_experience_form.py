from django.forms import ModelForm, DateInput
from django.core.exceptions import ValidationError
from app_forms.models import WorkExperience


class WorkExperienceForm(ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['position', 'company',
                  'start_date', 'end_date', 'description']
        labels = {
            'position': 'Cargo ',
            'company': 'Empresa ',
            'start_date': 'Data de início ',
            'end_date': 'Data de término ',
            'description': 'Descrição',
        }
        widgets = {
            'start_date': DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'}),
            'end_date': DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'})
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError('A data de término deve ser superior à data de início.')
        return cleaned_data