from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['titre', 'fichier']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre'}),
            'fichier': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
