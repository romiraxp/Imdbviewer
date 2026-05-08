from django import forms

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(
        label="Файл CSV",
        widget=forms.FileInput(attrs={
            'class': 'custom-file-input',
        })
    )