from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.list_persons, name='list_persons'),
    url(r'^person/(\d+)/$', views.person),
    url(r'^person/(\d+)/edit/$', views.person_edit),
    url(r'^message/$', views.message),
)
