from django.forms import ModelForm, CharField
from django import forms
from rent.models import RentBook


class CustomFirstNameField(CharField):
    def clean(self, value):
        value = super().clean(value)
        if value == value.lower() or value == value.upper():
            value = value.capitalize()
        return value


class CustomLastNameField(CharField):
    def clean(self, value):
        value = super().clean(value)
        if value == value.lower() or value == value.upper():
            value = value.capitalize()
        return value


class RentForm(ModelForm):
    class Meta:
        model = RentBook
        fields = ('book', 'first_name', 'last_name', 'email', 'phone', 'address', 'start_date', 'end_date',)
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

    first_name = CustomFirstNameField(max_length=50)
    last_name = CustomLastNameField(max_length=50)
