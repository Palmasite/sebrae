# -*- coding:utf-8 -*-
from django.forms.models import ModelForm
from social.models import Perfil,Profissional,Contato,RedeSocial

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

