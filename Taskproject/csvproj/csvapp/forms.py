from csvapp.models import Login,File
from django import forms


 
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Login
        fields='__all__'

class FileForm(forms.ModelForm):
    class Meta:
        model=File
        fields='__all__'