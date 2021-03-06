#-*- coding:utf-8 -*-

# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils import simplejson
from social.models import Perfil, Profissional, RedeSocial,Contato, Album
from social.forms import PerfilForm,ProfissionalForm,ContatoForm,RedeSocialForm, AlbumForm
from django.core.files.uploadedfile import SimpleUploadedFile


def perfil(request):
    if Perfil.objects.filter(user = request.session['username']) :
        perfil = Perfil.objects.filter(user = request.session['username'])
       
        formperfil = PerfilForm(instance = perfil[0])
        if request.method == 'POST':
            dados_form = PerfilForm(request.POST,request.FILES,instance = perfil[0])
            dados_form.save();
            #Perfil.objects.filter(pk = perfil).update(nome = request.POST["nome"],cargo = request.POST["cargo"],area = request.POST["area"],matricula =request.POST["matricula"],user = request.session['username'],foto = request.FILES['foto'])
            return HttpResponseRedirect('/perfil/profissional/')
    else:
        formperfil = PerfilForm(initial = {"user":request.session['username']})

    if request.method == 'POST':
        formperfil = PerfilForm(request.POST,request.FILES)
        formperfil.is_valid()
        formperfil.save()

    list_fotos = Album.objects.filter(user=request.session['username'])
    return render_to_response('perfil.html', locals(), context_instance=RequestContext(request))

def profissional(request):
    profissional_list = Profissional.objects.filter(user = request.session['username'])
    try:
        formperfil = ProfissionalForm(initial = {"user":request.session['username']})
        if request.method == "POST":
            formperfil = ProfissionalForm(request.POST)
            formperfil.is_valid()
            formperfil.save()
    except:
        pass
    return render_to_response('profissional.html', locals(), context_instance=RequestContext(request))

def contato(request):
    contato_list = Contato.objects.filter(user = request.session['username'])
    try:
        formperfil = ContatoForm(initial = {"user":request.session['username']})

        if request.method == "POST":
            formperfil = ContatoForm(request.POST)
            formperfil.is_valid()
            formperfil.save()
    except:
        pass
    return render_to_response('contato.html', locals(), context_instance=RequestContext(request))

def social(request):
    contato_list = RedeSocial.objects.filter(user = request.session['username'])
    try:
        formperfil = RedeSocialForm(initial = {"user":request.session['username']})

        if request.method == "POST":
            formperfil = RedeSocialForm(request.POST)
            formperfil.is_valid()
            formperfil.save()
            
    except:
        pass

    return render_to_response('redes.html', locals(), context_instance=RequestContext(request))
    
def album_foto(request):
    
    perfil_album = Perfil.objects.filter(user = request.session['username'])
    
    try:

        list_fotos = Album.objects.filter(user=request.session['username'])
          
        #formalbum = AlbumForm()
        formalbum = AlbumForm(initial = {"user":request.session['username']})
     
        if request.method == "POST":
            formalbum = AlbumForm(request.POST,request.FILES)
            formalbum.is_valid()
            formalbum.save()
            
    except:
        alerta = u"Não possui perfil. Favor adicionar um perfil"
    return render_to_response('album.html', locals(), context_instance=RequestContext(request))
   
   

def deletar(request,tabela,tabela_id):
    if tabela == "contato":
        Contato.objects.filter(pk = tabela_id ).delete()
        return HttpResponseRedirect('/perfil/contato/')
    elif tabela == "redes":
        RedeSocial.objects.filter(pk = tabela_id ).delete()
        return HttpResponseRedirect('/perfil/redes/')
    elif tabela == "profissional" :
        Profissional.objects.filter(pk = tabela_id ).delete()
        return HttpResponseRedirect('/perfil/profissional/')
    elif tabela == "foto_album":
        Album.objects.get(pk=tabela_id).delete()
        return HttpResponseRedirect('/perfil/album/')


def meuperfil(request, user_id):
  
    perfil = Perfil.objects.get(user = user_id)

    profissional_list = Profissional.objects.filter(user = user_id)
    contato_list = Contato.objects.filter(user = user_id)
    redes_list = RedeSocial.objects.filter(user = user_id)
    list_fotos = Album.objects.filter(user=user_id)

    return render_to_response('meuperfil.html', locals(), context_instance=RequestContext(request))
    


