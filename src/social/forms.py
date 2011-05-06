# -*- coding:utf-8 -*-
from django.forms.models import ModelForm
from social.models import Perfil,Profissional,Contato,RedeSocial,Album
from django.forms.widgets import *
from django.forms.fields import CharField, DateTimeField


class PerfilForm(ModelForm):
    class Meta:
        model = Perfil
        
class ProfissionalForm(ModelForm):
    class Meta:
        model = Profissional

class ContatoForm(ModelForm):
    class Meta:
        model = Contato

class RedeSocialForm(ModelForm):
    class Meta:
        model = RedeSocial
        
class AlbumForm(ModelForm):
    img_miniatura = CharField(required=False, widget = HiddenInput())
    #dat_foto = DateTimeField(required=False, widget = HiddenInput())
    class Meta:
        model = Album         

