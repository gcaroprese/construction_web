from django.conf.urls import patterns, include, url

from .views import (ContactCreateView, ContactSuccessView)

urlpatterns = patterns('',
    url(r'^$', ContactCreateView.as_view(), name='contact'),
    url(r'^exito/$', ContactSuccessView.as_view(), name='success'),
)

