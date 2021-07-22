from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

def check_email(str):
    length = len(str)
    comp = "nsut.ac.in"
    to_c = str[length-10:length]
    return to_c==comp


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def clean(self):
        cleaned_data=super(UserCreateForm, self).clean()
        flag = check_email(cleaned_data['email'])
        if flag == False:
            raise forms.ValidationError("must enter NSUT domain email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"
