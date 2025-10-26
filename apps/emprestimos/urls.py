from django.urls import path
from . import views

urlpatterns = [
    path('meus-emprestimos/', views.lista_emprestimos, name='lista_emprestimos'),
    path('solicitar-emprestimo/', views.solicitar_emprestimo, name='solicitar_emprestimo'),
    path('gerenciar-emprestimos/', views.gerenciar_emprestimos, name='gerenciar_emprestimos'),
    path('aprovar-emprestimo/<int:emprestimo_id>/', views.aprovar_emprestimo, name='aprovar_emprestimo'),
    path('negar-emprestimo/<int:emprestimo_id>/', views.negar_emprestimo, name='negar_emprestimo'),
    path('finalizar-emprestimo/<int:emprestimo_id>/', views.finalizar_emprestimo, name='finalizar_emprestimo'),
]