from django import forms
from .models import Order_all


class order_all_form(forms.ModelForm):
    class Meta :
        model = Order_all
        fields =[
            'Name',
            'Email',
            'Contact',
            'Address1',
            'Address2',
            'City',
            'State',
            'Pincode',
            'product'
        ]