from django.conf.urls import patterns, include, url

from .views import (LandingView, HomeView, AboutUsView)

urlpatterns = patterns('',
    url(r'^$', LandingView.as_view(), name='landing'),
    url(r'^inicio/$', HomeView.as_view(), name='home'),
    url(r'^estudio/$', AboutUsView.as_view(), name='about-us'),
)

