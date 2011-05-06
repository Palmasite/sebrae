#-*- coding: utf-8 -*-

from video.models import Video
from link.models import Link
from social.models import Perfil
from publicidade.models import Publicidade
from enquete.models import Enquete, Escolha
from configuracoes.models import Menu
from django.db import connection

import random 

def auth(request):
    #auth = False
    #if request.user.is_authenticated():
    #     auth = request.user
    #     user_perfil = Perfil.objects.get(user=auth)
    
    return locals()

def ultimo_video(request):
    #ultimo video
    ultimo_video = Video.objects.all()[:1]
    
    lista_imagem_video = ()
    
    
    for lv in ultimo_video:
        
        if lv.vch_url:
            video = lv.vch_url.split(" ")
            idvideo = video[3].split("/")
            idfoto = idvideo[4][:-1]
        
            lista_imagem_video = lista_imagem_video + ((lv.int_idvideo, lv.vch_titulo , lv.img_foto, idfoto,),)
        else:
            lista_imagem_video = lista_imagem_video + ((lv.int_idvideo, lv.vch_titulo , lv.img_foto,),)
        
    return locals()

def publicidade(request):
    #publicidade
    publicidade_topo = Publicidade.objects.filter(tipo="1")
    publicidade_direita = Publicidade.objects.filter(tipo="2")
    publicidade_rodape = Publicidade.objects.filter(tipo="3")
    publicidade_esquerda = Publicidade.objects.filter(tipo="4")
    publicidade_full_banner = Publicidade.objects.filter(tipo="5")
    
    
    #PUBLICIDADES RANDOMICAS
    
    publicidades = Publicidade.objects.select_related().filter(tipo = 2)
    if publicidades:
        publicidade1 = random.choice(publicidades.all())
        publicidade2 = random.choice(publicidades.all())
    
    
    
    return locals()

def enquete(request):
    enquete
    ultima_enquete = Enquete.objects.filter(boo_ativo = True ) [:1]
    enquete_esolhas = Escolha.objects.filter(enquete=ultima_enquete)
    
    return locals()

def links(request):
     #lista Links
    
    link_servico_destaque = Link.objects.filter(boo_destaque=True).filter(categoria=3)[:6]# para servicos
    link_rapidos = Link.objects.filter(categoria=4) #links rapidos
    link_rapidos_destaque = Link.objects.filter(categoria=1) #links rapidos destaque
    
    return locals()
    
def menu(request):
    menu_horizontal = Menu.objects.filter(tipo = 1)
    menu_vertical = Menu.objects.filter(tipo = 2)
    menu_rodape = Menu.objects.filter(tipo = 3)
    
    return locals()
