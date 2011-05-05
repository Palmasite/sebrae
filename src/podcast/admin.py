from django.contrib import admin 
from podcast.models import PodCast

from django.conf import settings


class AdminPodCast(admin.ModelAdmin):        
    class Media:
        model = PodCast
        js = (settings.MEDIA_URL + "/js/editorHtml/jscripts/tiny_mce/tiny_mce.js", # insere o javascript do editor html na pagina
              settings.MEDIA_URL + "/js/editorHtml/textarea.js",)# insere o javascript do editor html na pagina


admin.site.register(PodCast, AdminPodCast)



