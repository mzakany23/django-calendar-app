from django.contrib.auth.decorators import login_required
from models import CalendarEvent,EventType,EventColor
from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from django.core import serializers
from form import EventForm,EventId
import re
import datetime


@login_required
def events(request):
	events = CalendarEvent.objects.all()
	form = EventForm(request.POST or None)
	form2 = EventId()
	
	if form.is_valid():
		print 'works'
		id = request.POST['form_id']
		if id:
			form_contents = request.POST
			update_event(form_contents,id)
		else:
			create_event(form)
			# form = EventForm()
	else:
		print 'nope'


	grabbed_key = re.compile(r'(?P<apiKey>\w*)')
	api_key = grabbed_key.search(str(request.user.api_key)).group('apiKey')
	api = {
		'name' : request.user.username,
		'key' : api_key
	}
	context = {
		'events' : events,
		'api' : api,
		'form' : form,
		'form2' : form2
	}
	template = 'events/index.html'
	return render(request,template,context)

def create_event(form):
	form.save()

def delete_event(id):
	pass

def update_event(instance,id):
	event = CalendarEvent.objects.get(id=id)	
	type = EventType.objects.get(id=instance['type'])
	color = EventColor.objects.get(id=instance['color'])
	start = datetime.datetime.strptime(str(instance['start']), '%m/%d/%Y')
	end = datetime.datetime.strptime(str(instance['end']), '%m/%d/%Y')

	event.title = instance['title']
	event.type = type
	event.description = instance['description']
	event.start = start
	event.end = end
	event.color = color
	event.save()

@login_required
def event_edit(request,id):
	template = 'events/index.html'
	return render(request)

@login_required
def show(request):
	events = CalendarEvent.objects.all()
	context = {'events' : events}
	template = 'events/show.html'
	return render(request,template,context)




