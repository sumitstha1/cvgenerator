from django import forms 
from .models import User

class UserCvForm(forms.ModelForm):
    class Meta:
        fields = "__all__"
        model = User