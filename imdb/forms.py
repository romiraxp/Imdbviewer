# from django.forms import ModelForm
from django import forms
# from .models import Imdb, ImdbImport

# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username')
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

# class DeleteConfirmForm(forms.Form):
#     class Meta:
#         model = Imdb
#         fields = []
# class ImdbForm(ModelForm):
#     class Meta:
#         model = Imdb
#         fields = ['product_id', 'code', 'description', 'category', 'brand', 'manufacturer', 'status']
# class ImdbImportForm(ModelForm):
#     class Meta:
#         model = ImdbImport
#         fields = ('csv_file',)
#
# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(
    # widget = forms.TextInput(attrs={'size': 30, 'style': 'width: 200px;'})  # size в символах, style для CSS

    # username = forms.CharField(
        label="Файл CSV",
        widget=forms.FileInput(attrs={
            'class': 'custom-file-input',
            # 'style'
        })
    )