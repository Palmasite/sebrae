# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from agenda.views import *

urlpatterns = patterns('',
    (r'^eventos/$', 'agenda.views.eventos'),
    (r'^date/(?P<d>\d+)/(?P<m>\d+)/(?P<a>\d+)/$', 'agenda.views.date'),
    (r'^evento/(?P<eventos_id>\d+)/$', 'agenda.views.evento'),
)

