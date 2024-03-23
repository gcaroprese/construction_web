from django.conf.urls import patterns, include, url

from .views import (ProjectListView, ProjectDetailView)

urlpatterns = patterns('',
    url(r'^$', ProjectListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProjectDetailView.as_view(), name='detail'),
)

