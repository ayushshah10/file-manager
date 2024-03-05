from django import forms
from .models import FileUpload

class FileUploadForm(forms.ModelForm):
    # file = forms.FileField(widget = forms.TextInput(attrs={
    #         "type": "file",
    #         "multiple": "True",}))
     
    class Meta:
        model = FileUpload
        fields = ['file']
        widgets = {
            "file": forms.ClearableFileInput(attrs={'id': 'files', 'required': True})
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
     