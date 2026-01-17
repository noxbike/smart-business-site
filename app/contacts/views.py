from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    form = ContactForm()
    print(form)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            form.save()

            send_mail(
                subject="Thank you for your message",
                message="we have received your message and will get back to you shortly.",
                from_email="noxbike@gmail.com",
                recipient_list=[email],
                fail_silently=True,
            )

            send_mail(
                subject="New Contact Message Received",
                message=f"Message from {name}:\n\n{message}",
                from_email="noxbike@gmail.com",
                recipient_list=["jamesbond00439@gmail.com"],
                fail_silently=True,
            )
            return render(request, 'contacts/contact_success.html')
    else:
        form = ContactForm()    
        return render(request, 'contacts/contact.html', {'form': form})