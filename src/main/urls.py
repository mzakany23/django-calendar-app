from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from events.api import EventResource

event_resource =  EventResource()

# home
urlpatterns = patterns('',
	url(r'^$', 'front.views.home', name='home'),
  url(r'^admin/', include(admin.site.urls)),
)

# profile
urlpatterns += patterns('user_profile.views',
    url(r'^profile/', 'profile', name='profile'),
)

# events
urlpatterns += patterns('events.views',
	url(r'^calendar/edit/(?P<id>\d+)/$', 'event_edit',name='event_edit'),
    url(r'^calendar/', 'events', name='events'),
    url(r'^list/', 'show', name='events_show'),
)

# authentication
urlpatterns += patterns('front.views',
    url(r'^auth_login/', 'auth_login', name='login'),
    url(r'^logout/', 'auth_logout', name='logout'),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('',
    (r'^api/', include(event_resource.urls)),
)

