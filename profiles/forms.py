from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class userRegisterForm (UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=25, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["autocomplete"] = "username"
        self.fields["email"].widget.attrs["autocomplete"] = "email"
        self.fields["first_name"].widget.attrs["autocomplete"] = "given-name"
    
    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = (
            "phone_number",
            "address_line_1",
            "address_line_2",
            "town_or_city",
            "postcode",
            "country",
        )