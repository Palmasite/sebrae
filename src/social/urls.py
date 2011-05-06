# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from social.views import perfil, Album

urlpatterns = patterns('',
    (r'^perfil/', 'social.views.perfil'),
    (r'^profissional/', 'social.views.proficional'),
    (r'^contato/', 'social.views.contato'),
    (r'^redes/', 'social.views.social'),
    (r'^album/', 'social.views.album_foto'),
    

)
