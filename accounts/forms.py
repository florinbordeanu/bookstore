from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserProfile
from django.forms import ChoiceField, CharField, BooleanField
from accounts.models import genders


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


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')

    address = CharField()
    phone = CharField()
    gender = ChoiceField(choices=genders)
    accepted_terms = BooleanField()
    first_name = CustomFirstNameField(max_length=50)
    last_name = CustomLastNameField(max_length=50)

    def save(self, commit=True):
        user = super().save(commit=True)
        profile = UserProfile(user=user, phone=self.cleaned_data.get('phone'),
                              address=self.cleaned_data.get('address'),
                              gender=self.cleaned_data.get('gender'),
                              accepted_terms=self.cleaned_data.get('accepted_terms'))

        if commit:
            profile.save()
            return user
