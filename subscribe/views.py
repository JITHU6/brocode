from django.shortcuts import render
from brocode.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to Brocodeai'
        # message = 'Hope you are enjoying your Django Tutorials'
        user_name = str(sub['Name'].value())
        user_message = str(sub['Message'].value())
        user_email = str(sub['Email'].value())
        recepient = 'jithu.benny6@gmail.com'
        message = 'Message from'+user_name+'is '+user_message+' and his email is '+ user_email
        send_mail(subject,
            message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        return render(request, 'contact/contact.html', {'success': 'message send successfully'})
    return render(request, 'subscribe/index.html', {'form':sub})
