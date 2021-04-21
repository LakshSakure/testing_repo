
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
            handle_uploaded_file(request.FILES['profile_pic'])
            form.save()
            return redirect('/users/login')
    return render(request, 'register.html', {'form': form})

# def clean_file(self):
#     file = self.cleaned_data.get("file", False)
#     filetype = magic.from_buffer(file.read())
#     if not "XML" in filetype:
#         raise ValidationError("File is not XML.")
#     return file
def handle_uploaded_file(f):
    with open('media/pictures/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def login(request):
    loginForm = LoginFrom(request.POST)
    if loginForm.is_valid():
        loginForm.save()
    else:
        HttpResponse("Validation Error", content_type='text/plain')
    return render(request, 'login.html', {'form': loginForm})