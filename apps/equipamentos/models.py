from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Categoria")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Equipamento(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Equipamento")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    numero_serie = models.CharField(max_length=100, unique=True, verbose_name="Número de Série")
    descricao = models.TextField(blank=True, verbose_name="Descrição")
    disponivel = models.BooleanField(default=True, verbose_name="Disponível?")
    data_aquisicao = models.DateField(verbose_name="Data de Aquisição", auto_now_add=True)
    
    def __str__(self):
        return f"{self.nome} - {self.numero_serie}"
    
    class Meta:
        verbose_name = "Equipamento"
        verbose_name_plural = "Equipamentos"