from django import forms
from .models import FileUpload
#DataFlair #File_Upload
class Profile_Form(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = [
        'FileName',
        'UploadFile'
        ]