# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from social.views import perfil, Album

urlpatterns = patterns('',
    (r'^del/(?P<tabela>\w+)/(?P<tabela_id>\d+)/$', 'social.views.deletar'),
    (r'^perfil/', 'social.views.perfil'),
    (r'^profissional/', 'social.views.profissional'),
    (r'^contato/', 'social.views.contato'),
    (r'^redes/', 'social.views.social'),
    (r'^album/', 'social.views.album_foto'),
    (r'^videos/', 'social.views.video'),
    

)
