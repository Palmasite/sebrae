# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from social.views import *

urlpatterns = patterns('',
    (r'^del/(?P<tabela>\w+)/(?P<tabela_id>\d+)/$', 'social.views.deletar'),
    (r'^perfil/', 'social.views.perfil'),
    (r'^profissional/', 'social.views.profissional'),
    (r'^contato/', 'social.views.contato'),
    (r'^redes/', 'social.views.social'),
    (r'^meuperfil/(?P<user_id>\w+)/ver', 'social.views.meuperfil'),
    (r'^album/', 'social.views.album_foto'),
)
