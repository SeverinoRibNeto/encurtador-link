from django import forms
from .models import Links


class FormLinks(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormLinks, self).__init__(*args, **kwargs)
        self.required_css_class = 'form-control'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Links
        fields = "__all__"
