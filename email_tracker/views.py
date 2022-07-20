from django.shortcuts import render
from .forms import enteruser
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def index(request):
        if request.method =='POST':
            form = enteruser(request.POST)
            # check whether it's valid:
            if form.is_valid():
                name = request.POST['name']
                email = request.POST['email_address']
                message = request.POST['message']
                subject = request.POST['subject']

                email_from = settings.EMAIL_HOST_USER
                 #send an email
                send_mail(
                   subject , # subject
                   'Hello. This is' + name + '.' + message , # message
                    email_from, # from email
                    [email], # to email
                )
                
                return render(request, 'thankyou.html')
            
        else:
            form = enteruser()
            return render(request, 'input.html', {'form': form})