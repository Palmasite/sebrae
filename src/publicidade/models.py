# -*- ecoding: utf-8 -*-
from django.db import models
from thumbs import ImageWithThumbsField
from django.conf import settings 
import os
from datetime import datetime

def upload_to_foto(instance, name):
    extensao = os.path.splitext(name)[-1]
    data = datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    return os.path.join('fotopublicidade/', '%s%s' % (horario, extensao))

class Publicidade(models.Model):
    list_tipo = (('1', 'Topo'), ('2', 'Direita'), ('3', u'Rodapé'), ('4', 'Esquerda'), ('5', 'fullbanner'))
    idpublicidade = models.AutoField(primary_key=True)
    nome = models.CharField("Nome", max_length=250)

 
    img_foto = ImageWithThumbsField(verbose_name="Logomarca", upload_to=upload_to_foto, null=True, blank=True,)
    vch_arquivo = models.FileField("Flash", upload_to=upload_to_foto,null=True, blank=True,)
    tipo = models.CharField(u"Posição no portal", max_length=1, choices=list_tipo)
    dat_publicacao = models.DateField(u"Data Publicação",)

    def __unicode__(self):
        return unicode(self.nome)
    

        
        
    
