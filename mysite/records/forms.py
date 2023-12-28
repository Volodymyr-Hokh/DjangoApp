from django import forms

from .models import Record


class RecordForm(forms.ModelForm):
    tags = forms.CharField(label="Tags", help_text="Enter tags separated by space.")

    class Meta:
        model = Record
        fields = ["record"]
