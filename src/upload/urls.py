# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from upload.views import *

urlpatterns = patterns('',
    (r'^arquivos/a/$', 'upload.views.arquivos'),
    (r'^(?P<nome_galeria>\w+)/(?P<idgaleria>\d+)/$', 'upload.views.arquivos'),

)
