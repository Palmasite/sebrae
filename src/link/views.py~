# Create your views here.
from link.models import Categoria, Link
from django.template import RequestContext
from django.shortcuts import render_to_response

def todos_servicos(request):
    link_servico_destaque = Link.objects.filter(categoria = 3)[:6]# para servicos

    return render_to_response('mais_servico.html',locals(), context_instance=RequestContext(request))


def todos_links(request):

    lista_de_links = Link.objects.all()
    
    return render_to_response('todos_links.html',locals(), context_instance=RequestContext(request))
