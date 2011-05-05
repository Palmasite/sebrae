# Create your views here.
from social.models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson

from social.models import Perfil,Profissional,RedeSocial
from social.forms import PerfilForm,ProfissionalForm,ContatoForm,RedeSocialForm


def perfil(request):

    try:
        perfil = Perfil.objects.filter(user = "perfil")
        
            
        if request.method == 'POST':
            Perfil.objects.filter(pk = perfil).update(nome = request.POST["nome"],cargo = request.POST["cargo"],area = request.POST["area"],matricula =request.POST["matricula"]) 

        formperfil = PerfilForm(instance = perfil[0])
    except:
        formperfil = PerfilForm()

        if request.method == 'POST':
            formperfil = PerfilForm(request.POST,request.FILES)
            formperfil.is_valid()
            formperfil.save()
            
            
    return render_to_response('perfil.html', locals(), context_instance=RequestContext(request))
    
def proficional(request):
    
    profissional_list = Profissional.objects.filter(user = "perfil")
    
    try:
        formperfil = ProfissionalForm()
        
        if request.method == "POST":
            formperfil = ProfissionalForm(request.POST)
            formperfil.is_valid()
            formperfil.save()
    except:
        pass
    return render_to_response('profissional.html', locals(), context_instance=RequestContext(request))
    
def contato(request):
    contato_list = Contato.objects.filter(user = "perfil")
    try:
        formperfil = ContatoForm()
        
        if request.method == "POST":
            formperfil = ContatoForm(request.POST)
            formperfil.is_valid()
            formperfil.save()
    except:
        pass
    return render_to_response('perfil.html', locals(), context_instance=RequestContext(request))
    
def social(request):
    try:
        formperfil = RedeSocialForm()
        
        if request.method == "POST":
            formperfil = RedeSocialForm(request.POST)
            formperfil.is_valid()
            formperfil.save()
            formperfil.cleanned_data()
    except:
        pass
    return render_to_response('perfil.html', locals(), context_instance=RequestContext(request))
            


