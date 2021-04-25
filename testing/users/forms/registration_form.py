from django import forms
from users.models import Users

class UserForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['middle_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['mobile_number'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['email_id'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['address'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['city'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['gender'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['profile_pic'].widget.attrs.update({'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Users
        fields = ["first_name", "middle_name", "last_name", "mobile_number", "email_id", "address", "city", "gender", "profile_pic"]