from django.core.exceptions import ValidationError
from django.forms import ModelForm
from app_forms.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['phone', 'email','cep','state','city','address']
        labels = {
            'phone': 'Telefone ',
            'email': 'Email ',
            'state': 'Estado',
            'city': 'Cidade',
            'address': 'Endereço ',

        }
    def clean_cep(self):
        cep = self.cleaned_data.get('cep','')
        cep =''.join([char for char in cep if char.isdigit()])
        if len(cep) != 8:
            raise ValidationError('O CEP deve conter 8 dígitos')
        return cep

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        caracteres_para_remover = "().-"
        tabela = str.maketrans('', '', caracteres_para_remover)
        phone = phone.translate(tabela)
        return phone
