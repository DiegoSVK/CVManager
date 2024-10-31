from django.contrib import admin
from .models import PersonalData,Contact,WorkExperience,AcademicFormation




@admin.register(PersonalData)
class PersonalDataAdmin(admin.ModelAdmin):
    list_display = ['resume','first_name','last_name','age','birth_date','cpf','gender']
    search_fields = ['first_name','last_name','cpf']
    list_filter = ['gender','resume']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display =['resume','phone','email','address']
    search_fields = ['email']
    list_filter = ['resume']

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['resume','position','company','start_date','end_date','description']
    search_fields = ['position']
    list_filter = ['resume']

@admin.register(AcademicFormation)
class AcademicFormationAdmin(admin.ModelAdmin):
    list_display = ['resume','institution','course','start_date','end_date','additional_formations']
    search_fields = ['institution','course']
    list_filter = ['resume','institution','course']