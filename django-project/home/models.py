from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length = 300)
	email = models.EmailField(max_length = 30)
	subject = models.TextField()
	message = models.TextField()

	def __str__(self):
		return self.name
	
class Feedback(models.Model):
	name = models.CharField(max_length =300)
	post = models.CharField(max_length = 300)
	image = models.TextField()
	comments = models.TextField()

	def __str__(self):
		return self.name

class Information(models.Model):
	address = models.CharField(max_length = 300)
	address_info = models.CharField(max_length = 500)
	phone = models.CharField(max_length = 100)
	time = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 50)

	def __str__(self):
		return f'{self.address}{self.address_info}{self.phone}{self.time}{self.email}'

