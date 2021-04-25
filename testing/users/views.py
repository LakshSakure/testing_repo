
from users.forms.registration_form import UserForm
from users.forms.login_form import LoginFrom
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import os
from users.models import Users

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

def userList(request):
    userData = Users.objects.all().order_by('-id')
    i = 0
    data = []
    for value in userData:
        i +=1
        # src = value.profile_pic
        # profile_pic = "<img  src='/"+src+"' height='50' />"
        profile_pic =""
        data.append([i, value.add_date, value.id, value.first_name+" "+ value.last_name, value.email_id, value.mobile_number, value.address, value.city, profile_pic, value.gender, "", ""])

    return JsonResponse({"data": data}, status=200)
    # return HttpResponse(json_data, content_type="application/json")