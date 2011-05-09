# -*- coding:utf-8 -*-
from django.forms.models import ModelForm
from social.models import Perfil,Profissional,Contato,RedeSocial
from django import forms

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

