from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True, verbose_name="Matrícula")
    telefone = models.CharField(max_length=15, blank=True, verbose_name="Telefone")
    departamento = models.CharField(max_length=100, blank=True, verbose_name="Departamento")
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.matricula}"
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"