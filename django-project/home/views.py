from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
	views = {}
	views ['feedbacks'] = Feedback.objects.all()
	return render(request,'index.html', views)

def about(request):
	return render(request,'about.html')

def contact(request):
	views = {}
	views['information'] = Information.objects.all()


	if request.method == 'POST':
		na = request.POST['name']
		em = request.POST['email']
		sub = request.POST['subject']
		msg = request.POST['message']

		data = Contact.objects.create(
			name = na,
			email = em,
			subject = sub,
			message = msg
			)
		data.save()
	return render(request,'contact.html',views)

def price(request):

	return render(request,'price.html')

def services(request):

	return render(request,'services.html')

def portfolio(request):

	return render(request,'portfolio.html')

