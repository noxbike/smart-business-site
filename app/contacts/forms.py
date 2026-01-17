from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border rounded px-3 py-2',
                'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border rounded px-3 py-2',
                'placeholder': 'you@example.com'}),
            'message': forms.Textarea(attrs={
                'class': 'w-full border rounded px-3 py-2 h-32',
                'placeholder': 'Your message...'})}