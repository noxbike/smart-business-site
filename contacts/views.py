from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contacts/contact_success.html')
    return render(request, 'contacts/contact.html', {'form': form})