from django import forms
from .models import Donor
from django.db import IntegrityError

class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ['name', 'blood_group', 'address', 'phone_number']

    def save(self, commit=True):
        try:
            return super().save(commit=commit)
        except IntegrityError:
            self.add_error('phone_number', 'A donor with this phone number already exists.')
