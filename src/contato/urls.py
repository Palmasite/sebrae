from django.conf.urls.defaults import *
from contato.views import contato


urlpatterns = patterns('',
<<<<<<< HEAD
                       (r'^faleconosco/$', 'contato.views.contato'),
=======
                       (r'^contato/$', 'contato.views.contato'),
>>>>>>> 17abc77557000ce1f14b1c2b9687dd647f4e57ba
                       )

