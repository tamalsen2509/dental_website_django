from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
 


def home(request):
	return render(request,'home.html',{})


def contact(request):
	if request.method == "POST":	# setting up contact form conditions
		message_name = request.POST ['message-name']
		message_email = request.POST ['message-email']
		message = request.POST['message']

		# send email
		subject='Email confirmation'
		message_body='Hello we have received your email. Its a system generated email, please do not reply'
		from_user=settings.EMAIL_HOST_USER
		to_user=message_email
		
		send_mail(subject,message_body,from_user,to_user,fail_silently=True)
		

		return render(request,'contact.html',{'message_name':message_name})

	else: # return the page

		return render(request,'contact.html',{}) 

