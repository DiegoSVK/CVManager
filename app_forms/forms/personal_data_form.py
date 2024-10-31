from django.forms import ModelForm, DateInput
from django.core.exceptions import ValidationError
from app_forms.models import PersonalData
from django import forms


class PersonalDataForm(ModelForm):
    class Meta:
        model = PersonalData
        fields = ['first_name', 'last_name', 'age',
                  'birth_date', 'cpf', 'gender']

        labels = {
            'first_name': 'Nome ',
            'last_name': 'Sobrenome ',
            'birth_date': 'Data de nascimento ',
            'age': 'Idade',
            'cpf': 'CPF ',
            'gender': 'Gênero '

        }
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'}),
            'age':forms.TextInput(attrs={'type': 'text'}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        clean_caracter =".-_"
        table = str.maketrans('','',clean_caracter)
        cpf = cpf.translate(table).strip()

        if len(cpf) != 11:
            raise ValidationError(
                'CPF inválido. Deve conter exatamente 11 dígitos numéricos.')
        if not cpf.isdigit():
            raise ValidationError('O CPF deve conter apenas números.')
        return cpf


    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise ValidationError('Apenas pessoas maiores de 18 anos.')
        return age


    def clean(self):
        cleaned_data = super().clean()
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        if first_name and last_name:
            if first_name == last_name:
                raise ValidationError('Nome e Sobrenome não podem ser iguais.')
        return cleaned_data
