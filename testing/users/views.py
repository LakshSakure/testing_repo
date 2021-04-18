from django.shortcuts import render
from users.forms.registration_form import UserForm
from users.models import Users
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/login')
    else:
        return HttpResponse("Form valiation Failed", content_type='text/plain')
    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'login.html')