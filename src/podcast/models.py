#-*- coding:utf-8 -*-
from django.db import models
import os
from datetime import datetime


def upload_to_musica(instance, name):
    extensao = os.path.splitext(name)[-1]
    data = datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    return os.path.join('podcast/', '%s%s' % (horario, extensao))


class PodCast(models.Model):
    idpoadcast = models.AutoField(primary_key=True)
    vch_titulo = models.CharField("Titulo", max_length=500)
    vch_arquivo = models.FileField("Mp3", upload_to=upload_to_musica,null=True, blank=True,)
    dat_publicacao = models.DateTimeField("Data Publicação")
    
    def __unicode__(self):
        return unicode(self.vch_titulo)
        
        


