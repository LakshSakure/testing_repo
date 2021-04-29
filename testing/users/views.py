from rest_framework.generics import get_object_or_404
from users.forms.registration_form import UserForm
from users.forms.login_form import LoginFrom
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from users.models import Users
import os

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
        gen ="other"
        if value.gender == 1: gen ="Male"
        elif value.gender == 2: gen = "Female"
        # title = "Edit User"+value.first_name+" "+value.last_name
        edit = "<a onclick='openEdit("+str(value.id)+", ` Edit User: "+value.first_name+" "+value.last_name+"`, `update_user_form` )' ><i class='btn btn-secondary btn-hover btn-sm fa fa-edit' > Edit</i></a>"

        profile_pic =""
        data.append([i, value.add_date, value.id, value.first_name+" "+ value.last_name, value.email_id, value.mobile_number, value.address, value.city, profile_pic, gen, edit])

    return JsonResponse({"data": data}, status=200)
    # return HttpResponse(json_data, content_type="application/json")

def userEditView(request):
    userData = []
    if request.method == "POST":
        id = request.POST.get('id')
        userData = Users.objects.get(id = id)
        edit_form = UserForm(instance= userData)
    return render(request, 'user_edit.html', {'form': edit_form, 'id': id})

def updateUser(request):
    if request.method == "POST":
        id = request.POST.get('id')
        instance = get_object_or_404(Users, id=id)
        form = UserForm(request.POST or None,request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return JsonResponse({'error': 0, 'msg': 'updated Successfully'}, status=200)
        else:
            return JsonResponse({'error': 1, 'msg': 'Something going wrong'}, status=200)
