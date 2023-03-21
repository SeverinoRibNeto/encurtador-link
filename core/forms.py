from django import forms
from models import Links


class FormLinks(forms.Form):
    class Meta:
        model = Links
        fields = "__all__"
