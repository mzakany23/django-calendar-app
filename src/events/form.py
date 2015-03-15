from django import forms
from models import CalendarEvent,EventColor,EventType

class EventForm(forms.ModelForm):
	class Meta:
		model = CalendarEvent
		fields = ['title','type','description','start','end','color']

	
	title = forms.CharField(widget=forms.TextInput(attrs={
		"class" : "form-control",
		"id" : "inputTitle",
		"placeholder" : "Title"
	}))

	
	start = forms.DateField(widget=forms.TextInput(attrs={
		"class" : "form-control",
		"id" : "datePicker1",
		"placeholder" : "Date"
	}))

	end = forms.DateField(widget=forms.TextInput(attrs={
		"class" : "form-control",
		"id" : "datePicker2",
		"placeholder" : "Date"
	}))

class EventId(forms.Form):
	form_id = forms.CharField(widget=forms.TextInput(attrs={
		'id' : 'eventobjid',	
		'style' :	 'display: none;'
	}));
