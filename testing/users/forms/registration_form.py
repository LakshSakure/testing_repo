from django import forms
from users.models import Users

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Users
        fields = ["first_name", "middle_name", "last_name", "mobile_number", "email_id", "address", "city", "gender"]
        # first_name = forms.CharField(required=True, max_length=50)
        # middle_name = forms.CharField(required=True, max_length=50)
        # last_name = forms.CharField(required=True, max_length=50)
        # mobile_number = forms.CharField(required=True, max_length=15, min_length=10)
        # email_id = forms.EmailField(required=True)
        # address = forms.TextInput()
        # city = forms.CharField(required=True, max_length=50)
        #
        # first_name.widget.attrs.update({'class': 'form-control'})
        # middle_name.widget.attrs.update({'class': 'form-control'})
        # last_name.widget.attrs.update({'class': 'form-control'})

        # fields = [first_name, middle_name, last_name, mobile_number, email_id, address, city]