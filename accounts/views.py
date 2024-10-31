
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms.registration_form import RegistrationForm




def registration_view(request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('sucesso')
        else:
            for error in form.errors.values():
                messages.error(request,error)
    else:
        form = RegistrationForm()

    return render(request,'auth/registration.html',{'form': form})


def success_view(request):
   return render(request,'auth/success.html')



def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request,username = username,password = password)
            if user:
                login(request,user)
                return redirect('cv_platform')
            else:
                messages.error(request,'Nome de usuário ou senha incorretos.',extra_tags='login_error')
        else:
            messages.error(request,'Por favor, preecha todos os campos.',extra_tags='login_error')
    return render(request,'auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')



