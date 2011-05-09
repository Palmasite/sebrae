#-*- coding: utf-8 -*-
from django.http import HttpResponse

class MeuMiddleware(object):
    testar = False

    def process_request(self, request):
        if 'testar' in request.GET:
            self.testar = True
            request.GET._mutable = True
            request.GET.pop('testar')

        if request.session.get('projeto_selecionado', None):
            try:
                request.projeto = 
            except TypeError:
                request.projeto = None
        else:
            request.projeto = None

    def process_response(self, request, response):
        if self.testar:
            response.content = response.content.replace('</body>', '<b>EM TESTE</b></body>')
        
        return response

