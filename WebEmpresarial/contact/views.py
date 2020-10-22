from django.shortcuts import render, redirect
from contact.forms import ContactForm
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.
def contact(request):
    print("Tipo de metodo: {}", request.method)
    contactform = ContactForm(data=request.POST)
    if contactform.is_valid():
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        content = request.POST.get('content', '')

        email = EmailMessage(
            "Cafeteria: La Caffetiera",
            "De {} <{}>\n\n{}".format(name, email, content),
            "no_contestar",
            ["jessica.tapia.soria@gmail.com"],
            reply_to=[email]
        )
        try:
            email.send()
            return redirect(reverse('contact')+"?ok")
        except:
            return redirect(reverse('contact')+"?fail")

    return render(request, 'contact/contact.html', {'form': contactform})
