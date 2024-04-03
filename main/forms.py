from django import forms

from main.models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ["subject", "message", "fullname", "email"]
