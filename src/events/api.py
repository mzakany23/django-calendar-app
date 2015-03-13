from tastypie.resources import ModelResource
from models import CalendarEvent
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization,DjangoAuthorization

class EventResource(ModelResource):
  class Meta:	
  	# c75ba470b5814154c1e0b380dfe1a09fbce1e437
    queryset = CalendarEvent.objects.all()
    allowed_methods = ['get','post','delete']
    resource_name = 'event/list'
    authentication = ApiKeyAuthentication()
    
