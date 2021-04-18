from django import forms
from users.models import Users

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["first_name", "middle_name", "last_name", "mobile_number", "email_id", "address", "city"]