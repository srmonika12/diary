from django import forms
from .models import entry

class EntryForm(forms.ModelForm):
    class Meta:
        model=entry
        fields="__all__"