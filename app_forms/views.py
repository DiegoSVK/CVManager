from django.contrib import  messages

from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from .forms import PersonalDataForm, ContactForm, WorkExperienceForm, AcademicFormationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PersonalData, Contact, WorkExperience, AcademicFormation
from cv_platform.models import Resume





@method_decorator(login_required(login_url="login"), name='dispatch')
class FormWizard(SessionWizardView):
    form_list = [PersonalDataForm, ContactForm,
                 WorkExperienceForm, AcademicFormationForm]
    template_name = 'formularios/form_wizard.html'

    def get(self, request, *args, **kwargs):

        storage = messages.get_messages(self.request)
        storage.used = True
        return super().get(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        title_resume = self.request.session.get('title_resume')
        resume = Resume.objects.create(title=title_resume, user=self.request.user)

        for form in form_list:
            if form.is_valid():
                cleaned_data = form.cleaned_data
                try:
                    if isinstance(form, PersonalDataForm):
                        personal_data = PersonalData(**cleaned_data)
                        personal_data.resume =resume
                        personal_data.save()
                    if isinstance(form, ContactForm):
                        contact_form = Contact(**cleaned_data)
                        contact_form.resume = resume
                        contact_form.save()
                    if isinstance(form, WorkExperienceForm):
                        work_experience = WorkExperience(**cleaned_data)
                        work_experience.resume = resume
                        work_experience.save()
                    if isinstance(form, AcademicFormationForm):
                        academic = AcademicFormation(**cleaned_data)
                        academic.resume = resume
                        academic.save()


                except Exception as e:
                    messages.error(self.request,f'Erro ao salvar formulário:{e}',extra_tags='form_error')
                    return redirect('cv_platform')

        self.request.session['form_success']= 'Formulário salvo com sucesso.'
        return redirect('cv_platform')

