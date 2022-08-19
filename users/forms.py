from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile


User = get_user_model()


class CreatonForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("externalid", "accesstoken")

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["externalid"].widget.attrs["disabled"] = "disabled"
        self.fields["accesstoken"].widget.attrs["disabled"] = "disabled"
        for name, field in self.fields.items():
            field.widget.attrs["style"] = "width:500px; height:30px;"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs["style"] = "width:500px; height:30px;"
