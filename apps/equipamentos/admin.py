from django.contrib import admin
from .models import Categoria, Equipamento

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'numero_serie', 'disponivel', 'data_aquisicao']
    list_filter = ['categoria', 'disponivel', 'data_aquisicao']
    search_fields = ['nome', 'numero_serie', 'descricao']
    list_editable = ['disponivel']
