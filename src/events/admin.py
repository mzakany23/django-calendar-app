from django.contrib import admin

from models import CalendarEvent,EventType,EventColor

class CalendarEventAdmin(admin.ModelAdmin):
	list_display = ['type','start','end','color']
	list_editable = ['type','start','end','color']

	class Meta:
		model = CalendarEvent

class EventTypeAdmin(admin.ModelAdmin):
	class Meta:
		model = EventType

class EventColorAdmin(admin.ModelAdmin):
	class Meta:
		model = EventColor

admin.site.register(CalendarEvent,CalendarEventAdmin)
admin.site.register(EventType,EventTypeAdmin)
admin.site.register(EventColor,EventColorAdmin)