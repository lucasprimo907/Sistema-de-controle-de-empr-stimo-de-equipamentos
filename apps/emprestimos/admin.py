from django.contrib import admin
from .models import Emprestimo

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ['equipamento', 'usuario', 'data_solicitacao', 'data_devolucao_prevista', 'status']
    list_filter = ['status', 'data_solicitacao', 'data_devolucao_prevista']
    search_fields = ['equipamento__nome', 'usuario__username', 'observacoes']
    list_editable = ['status']
    date_hierarchy = 'data_solicitacao'
