from django.http import HttpResponse
from django.shortcuts import render, redirect


# Contact form
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail, BadHeaderError

def index(request):
    return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio.html')

def merchandise(request):
    return render(request, 'merchandise.html')


def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')

            try:
                send_mail(contact_name, form_content, contact_email, ['hanh00hoang@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, 'contact.html', {'form': form_class})

def success(request):
    #return HttpResponse('Success! Thank you for your message.')
    return render(request, 'success.html')