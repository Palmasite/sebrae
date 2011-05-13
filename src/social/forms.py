# -*- coding:utf-8 -*-
from django.forms.models import ModelForm
from django import forms
from social.models import Perfil,Profissional,Contato,RedeSocial,Album
from django.forms.widgets import *
from django.forms.fields import CharField, DateTimeField

class PerfilForm(ModelForm):
    user = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Perfil
        
class ProfissionalForm(ModelForm):
    user = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Profissional

class ContatoForm(ModelForm):
    user = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Contato

class RedeSocialForm(ModelForm):
    user = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = RedeSocial
        
class AlbumForm(ModelForm):
    img_miniatura = CharField(required=False, widget = HiddenInput())
    user = forms.CharField(widget=forms.HiddenInput())
    #dat_foto = DateTimeField(required=False, widget = HiddenInput())
    class Meta:
        model = Album
        

