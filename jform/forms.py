from .models import Register
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = "__all__"
        labels = {'fullname': "Name", "mobile_number": "Mobile Number"}