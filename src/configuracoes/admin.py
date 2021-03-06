#-*- coding: utf-8 -*-
from django.contrib import admin
from configuracoes.models import Modulo, Layout, Menu,Item_Menu
from admin_utils import MeuModelAdmin, MeuTabularInline 


class AdminItem(MeuTabularInline):
    model = Item_Menu
    
class MenuAdmin(MeuModelAdmin):
    model = Menu
    inlines = [AdminItem, ]
    

class LayoutAdmin(admin.ModelAdmin):
    list_display = ('topobg', 'topo', 'logo', 'menufundo',)
    model = Layout

admin.site.register(Layout, LayoutAdmin)
admin.site.register(Modulo)
admin.site.register(Menu,MenuAdmin)



