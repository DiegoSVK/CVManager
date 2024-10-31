from django.urls import path
from .views import  FormWizard

urlpatterns = [

    path('', FormWizard.as_view(), name='form_wizard'),
]
