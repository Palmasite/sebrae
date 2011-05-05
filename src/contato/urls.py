from django.conf.urls.defaults import *
from contato.views import contato


urlpatterns = patterns('',

    (r'^faleconosco/$', 'contato.views.contato'),
    (r'^contato/$', 'contato.views.contato'),

)

