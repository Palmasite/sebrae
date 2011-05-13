# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from dirigente.views import dirigente


urlpatterns = patterns('',
    (r'^todos/dirigentes/$', 'dirigente.views.dirigente'),

)
