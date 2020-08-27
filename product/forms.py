from django import forms
from .models import contactus



class contact_form(forms.ModelForm):
    class Meta:
        model =contactus
        fields=['name','gmail','contact','message']