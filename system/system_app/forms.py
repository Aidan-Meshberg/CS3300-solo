from django import forms
from .models import *


class AddDay(forms.ModelForm):
    class Meta:
        model = Day_to_Day
        fields = ['time', 'location', 'money_spent']
        labels = {
            'time': 'Time',
            'location': 'Where was money spent?',
            'money_spent': 'How much money was spent?'
        }

class updateDiem(forms.ModelForm):
    class Meta:
        model = Per_Diem
        fields = ['title', 'about', 'contact_email', 'phone_number']
        labels = {
            'title': 'Title',
            'about': 'About',
            'contact_email': 'Contact email',
            'phone_number': 'Phone number'
        }