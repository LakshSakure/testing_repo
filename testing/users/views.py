
from users.forms.registration_form import UserForm
from users.forms.login_form import LoginFrom
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/users/login')
    return render(request, 'register.html', {'form': form})

def login(request):
    loginForm = LoginFrom(request.POST)
    if loginForm.is_valid():
        loginForm.save()
    else:
        HttpResponse("Validation Error", content_type='text/plain')
    return render(request, 'login.html', {'form': loginForm})