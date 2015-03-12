from django.db import models

class EventColor(models.Model):
	name = models.CharField(max_length=40,null=True)
	color = models.CharField(max_length=40,default='#009900')
	def __unicode__(self):
		return self.name

class EventType(models.Model):
	name = models.CharField(max_length=140)
	description = models.TextField(max_length=500,null=True)
	def __unicode__(self):
		return self.name

class CalendarEvent(models.Model):
	title = models.CharField(max_length=40,null=True,blank=True)
	type = models.ForeignKey(EventType)
	description = models.TextField(null=True,blank=True)
	start = models.DateField()
	end = models.DateField(null=True,blank=True)
	color = models.ForeignKey(EventColor,null=True)
	
	def __unicode__(self):
		return self.type.name

