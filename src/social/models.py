# -*-ecoding:utf-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField
from django.conf import settings

from django.contrib.auth.models import User
import os

from datetime import datetime




def upload_to_foto_perfil(instance, name):
    extensao = os.path.splitext(name)[-1]
    nome = os.path.splitext(name)[0]
    data = datetime.now()
    horario = str(nome) + "-" + str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    #raise Exception(os.path.join('%s/'%(pasta_galeria),'%s%s'%(horario, extensao)))
    #return os.path.join('galeria/%s/' % (pasta_galeria), '%s%s' % (horario, extensao))
    return os.path.join('foto_social/perfil/', '%s%s'%(horario, extensao))

class Perfil(models.Model):
    nome = models.CharField("Nome", max_length=250)
    cargo = models.CharField("Cargo", max_length=250)
    area = models.CharField(u"Área", max_length=250)
    datanascimento = models.DateField("Data de Nascimento")
    matricula = models.CharField("Matricula", max_length=250)
    user = models.CharField("UserName", max_length=250)
    foto = ImageWithThumbsField(verbose_name="Foto ", upload_to= upload_to_foto_perfil, sizes=((110, 160),), null=True, blank=True,)
    
    
    def save(self):
        super(Perfil, self).save()
     
        foto = str(self.foto)
        if foto != '':        
            f = str(foto).split('.') 
            """ Renomeia img_foto"""
            if not "110x160" in f:    
                self.foto = f[0] + '.110x160.' + f[1]
                os.remove(settings.MEDIA_ROOT + '/' + foto)
                        
            super(Perfil, self).save()
            """ Apaga a foto original da pasta """
        else:
            super(Perfil, self).save()
        
    def __unicode__(self):
        return unicode(self.nome)
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"



class Profissional(models.Model):
    list_tipo = (('1', u'Profissão'), ('2', u'Especialização'))    
    formacao = models.CharField(u"Formação", max_length=250)
    instituicao = models.CharField(u"Instituição", max_length=250)
    local = models.CharField("Local", max_length=250)
    tipo = models.CharField("Tipo", max_length=2, choices=list_tipo)    
    user = models.CharField("UserName", max_length=250)
    
    def __unicode__(self):
        return unicode(self.vch_formacao)

class Contato(models.Model):
    list_tipo = (('1', 'Fone/Ramal'), ('2', 'Cel. trabalho'), ('3', 'Cel. pessoal'), ('4', 'Email trabalho'), ('5', 'Email pessoal'),)
    idcontato = models.AutoField(primary_key=True)
    contato = models.CharField("Contato", max_length=250)
    tipo = models.CharField("Tipo", max_length=2, choices=list_tipo)    
    user = models.CharField("UserName", max_length=250)
    
    def __unicode__(self):
        return unicode(self.vch_contato)
    
    
class RedeSocial(models.Model):
    list_tipo = (('1', 'Orkut'), ('2', 'Facebook'), ('3', 'MSN'))  
    int_idcontato = models.AutoField(primary_key=True)
    rede = models.CharField("Contato", max_length=250)
    vch_tipo = models.CharField("Tipo", max_length=2, choices=list_tipo)    
    user = models.CharField("UserName", max_length=250)
    
    
def upload_to_foto(instance, name):
    extensao = os.path.splitext(name)[-1]
    nome = os.path.splitext(name)[0]
    data = datetime.now()
    horario = str(nome) + "-" + str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    #raise Exception(os.path.join('%s/'%(pasta_galeria),'%s%s'%(horario, extensao)))
    #return os.path.join('galeria/%s/' % (pasta_galeria), '%s%s' % (horario, extensao))
    return os.path.join('foto_social/galeria/', '%s%s'%(horario, extensao))


class Album(models.Model):
    int_idbancoimagem = models.AutoField(primary_key=True)
    vch_titulo = models.CharField("Título Foto", max_length=250)
    img_foto = ImageWithThumbsField(verbose_name="Foto", upload_to=upload_to_foto, sizes=((150, 85), (800, 600)))
    img_miniatura = models.CharField(max_length=100, null=True, blank=True) 
    user = models.CharField('User', max_length=250)
    
    def save(self):
        super(Album, self).save()
        
        foto = str(self.img_foto)        
        f = str(foto).split('.')  
        """ Renomeia img_foto"""    
        self.img_foto = f[0] + '.800x600.' + f[1]
        """ Renomeia img_miniatura"""    
        self.img_miniatura = f[0] + '.150x85.' + f[1]
        super(Album, self).save()
        """ Apaga a foto original da pasta """
        os.remove(settings.MEDIA_ROOT + '/' + foto)
    
    """ funcao que coloca as imagens no campo img_foto na consulta """
    def foto(self):
        foto = str(self.img_miniatura)
    
        img = '<img src="/espiga/media/' + foto + '"/>'       
        return img

    foto.allow_tags = True 
   
    def __unicode__(self):
        return self.vch_titulo
    
    class Meta:
        verbose_name = "Banco de Imagem"
        verbose_name_plural = "Banco de Imagem"
        
     
