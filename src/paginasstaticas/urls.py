# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from paginasstaticas.views import pagina

urlpatterns = patterns('',
    (r'^(?P<url_categoria>\w+)/(?P<url>\w+)/$', 'paginasstaticas.views.pagina'),

)
