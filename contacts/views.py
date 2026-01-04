from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    form = ContactForm()
    return render(request, 'contacts/contact.html', {'form': form})