from django.conf.urls.defaults import *

from link.views import todos_servicos, todos_links




urlpatterns = patterns('',
    (r'^maisservicos/', 'link.views.todos_servicos'),

    (r'^todos/', 'link.views.todos_links')
                       

)
