# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from podcast.views import pod

urlpatterns = patterns('',
    (r'^mais/podcasts/$', 'podcast.views.pod'),

)
