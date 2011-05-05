from django.contrib import admin 
from dirigente.models import Dirigente

from django.conf import settings


class AdminDirigente(admin.ModelAdmin):        
    class Media:
        model = Dirigente
        js = (settings.MEDIA_URL + "/js/editorHtml/jscripts/tiny_mce/tiny_mce.js", # insere o javascript do editor html na pagina
              settings.MEDIA_URL + "/js/editorHtml/textarea.js",)# insere o javascript do editor html na pagina


admin.site.register(Dirigente, AdminDirigente)



