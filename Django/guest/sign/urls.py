from django.conf.urls import url
from sign import views_if
from sign import views_if,views_if_sec
urlpatterns=[
	url(r'^add_guest/',views_if.add_guest,name='add_guest'),
	url(r'^get_event_list/',views_if.get_event_list,name='get_event_list'),
	url(r'^add_event/',views_if.add_event,name='add_event'),
	url(r'^sec_get_event_list/',views_if_sec.get_event_list,name='get_event_list'),
	url(r'^sec_add_event/',views_if_sec.add_event,name='add_event'),
	]