from django.conf.urls import url
from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='main'),
    url(r'^student/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^check/$', views.Check.as_view(), name='check'),
]