from tkinter.font import names

from django.urls import path
from .views import login_view,registration_view,success_view

urlpatterns = [
    path('', login_view, name='login'),
    path('cadastro/',registration_view,name='registration'),
    path('sucesso/',success_view,name='sucesso'),

]
