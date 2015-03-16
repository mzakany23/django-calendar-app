from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	image = models.ImageField(upload_to='images')
	account = models.OneToOneField(User)
	
	def __unicode__(self):
		return self.account.username


