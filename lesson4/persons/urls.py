from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.list_persons, name='list_persons'),
    url(r'^person/(\d+)/$', views.person),
    url(r'^person/(\d+)/edit/$', views.person_edit),
    url(r'^message/$', views.message),
    # url(r'^simple/$', views.simple),
    # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
