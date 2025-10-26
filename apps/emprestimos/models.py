from django.db import models
from django.contrib.auth.models import User
from apps.equipamentos.models import Equipamento

class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('negado', 'Negado'),
        ('ativo', 'Ativo'),
        ('finalizado', 'Finalizado'),
        ('atrasado', 'Atrasado'),
    ]

    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, verbose_name="Equipamento")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuário")
    data_solicitacao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Solicitação")
    data_emprestimo = models.DateTimeField(null=True, blank=True, verbose_name="Data do Empréstimo")
    data_devolucao_prevista = models.DateField(verbose_name="Data de Devolução Prevista")
    data_devolucao_real = models.DateTimeField(null=True, blank=True, verbose_name="Data de Devolução Real")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente', verbose_name="Status")
    observacoes = models.TextField(blank=True, verbose_name="Observações")
    
    def __str__(self):
        return f"{self.equipamento.nome} - {self.usuario.username}"
    
    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ['-data_solicitacao']