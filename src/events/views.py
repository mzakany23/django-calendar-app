from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import CalendarEvent,EventType,EventColor
from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from django.core import serializers
from form import EventForm,EventId
import re
import datetime

def delete(request,id):
	try: 
		event = CalendarEvent.objects.get(id=id)
		event.delete()
	except:
		pass

	return HttpResponseRedirect('/')

def detail(request,id):
	form = EventForm(request.POST or None)
	try:
		event = CalendarEvent.objects.get(id=id)
	except:
		event = ''

	context = {'event' : event, 'form' : form}
	template = 'events/detail.html'
	return render(request,template,context)

def search(request):
	try:
		text = request.GET.get('search_text')
	except:
		text = ''

	events = CalendarEvent.objects.filter(title__contains=text)
	template = 'events/ajax_search.html'
	context = {'events' : events}
	return render(request,template,context)

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
			form = EventForm()
		else:
			create_event(form)
			form = EventForm()
	else:
		print 'nope'


	grabbed_key = re.compile(r'(?P<apiKey>\w*)')
	try:
		api_key = grabbed_key.search(str(request.user.api_key)).group('apiKey')
	except: 
		api_key = None
		
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
	try:
		
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
	except:
		pass

@login_required
def event_edit(request,id):
	template = 'events/index.html'
	return render(request)

@login_required
def list(request):
	events = CalendarEvent.objects.all()
	paginator = Paginator(events, 5)
	page = request.GET.get('page')
	try: 
		event_list = paginator.page(page)
	except PageNotAnInteger:
		event_list = paginator.page(1)
	except EmptyPage:
		event_list = paginator.page(paginator.num_pages)
	list_range = []

	for i in range(paginator.num_pages):
		list_range.append(i+1)

	context = {'events' : event_list, 'list_range' : list_range}
	template = 'events/show.html'
	return render(request,template,context)




