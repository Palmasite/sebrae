#-*- coding:utf-8 -*-

from django.db import models
import os
from datetime import datetime
from thumbs import ImageWithThumbsField
from django.conf import settings



# Create your models here

def upload_to_foto(instance, name):
    extensao = os.path.splitext(name)[-1]
    data = datetime.now()
    horario = str(data.day) + '_' + str(data.month) + '_' + str(data.year) + '_' + str(data.hour) + '_' + str(data.minute) + '_' + str(data.second)
    return os.path.join('fotodirigente/', '%s%s' % (horario, extensao))


class Dirigente(models.Model):
    iddirigente = models.AutoField(primary_key = True)
    nome = models.CharField('Nome', max_length=200,)
    descricao = models.TextField("Descrição")
    img_foto = ImageWithThumbsField(verbose_name="Logomarca", upload_to=upload_to_foto,sizes=((100, 100),), null=True, blank=True,)
    
    
    def __unicode__(self):
        return unicode(self.nome)
    
    def save(self, force_insert=False, force_update=False):
        super(Dirigente, self).save(force_insert, force_update)
        foto = str(self.img_foto)
        if foto != '':        
            f = str(foto).split('.') 
            """ Renomeia img_foto"""
            if not "100x100" in f:    
                self.img_foto = f[0] + '.100x100.' + f[1]
                os.remove(settings.MEDIA_ROOT + '/' + foto)
                        
            super(Dirigente, self).save(force_insert, force_update)
            """ Apaga a foto original da pasta """
            
        else:
            super(Dirigente, self).save(force_insert, force_update)
