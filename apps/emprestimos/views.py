from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils import timezone
from .models import Emprestimo
from apps.equipamentos.models import Equipamento

#Função para ver se é staff ou admin
def is_staff_user(user):
    return user.is_staff

@login_required
def lista_emprestimos(request):
    #vai Mostrar todos os empréstimos do usuário logado
    meus_emprestimos = Emprestimo.objects.filter(usuario=request.user).order_by('-data_solicitacao')
    
    context = {
        'meus_emprestimos': meus_emprestimos,
    }
    return render(request, 'emprestimos/lista.html', context)

@login_required
def solicitar_emprestimo(request):
    equipamentos_disponiveis = Equipamento.objects.filter(disponivel=True)
    
    if request.method == 'POST':
        equipamento_id = request.POST.get('equipamento')
        data_devolucao = request.POST.get('data_devolucao')
        observacoes = request.POST.get('observacoes', '')
        
        equipamento = get_object_or_404(Equipamento, id=equipamento_id)
        
        # Criar o emprestimo
        emprestimo = Emprestimo(
            equipamento=equipamento,
            usuario=request.user,
            data_devolucao_prevista=data_devolucao,
            observacoes=observacoes,
            status='pendente'
        )
        emprestimo.save()
        
        messages.success(request, 'Solicitação de empréstimo enviada com sucesso! Aguarde aprovação.')
        return redirect('lista_emprestimos')
    
    context = {
        'equipamentos_disponiveis': equipamentos_disponiveis,
        'hoje': timezone.now().date()
    }
    return render(request, 'emprestimos/solicitar.html', context)

@login_required
@user_passes_test(is_staff_user)
def gerenciar_emprestimos(request):
    # Todos os empréstimos que estão pendentes e ativos
    emprestimos_pendentes = Emprestimo.objects.filter(status='pendente').order_by('-data_solicitacao')
    emprestimos_ativos = Emprestimo.objects.filter(status='ativo').order_by('-data_emprestimo')
    emprestimos_todos = Emprestimo.objects.all().order_by('-data_solicitacao')
    
    context = {
        'emprestimos_pendentes': emprestimos_pendentes,
        'emprestimos_ativos': emprestimos_ativos,
        'emprestimos_todos': emprestimos_todos,
    }
    return render(request, 'emprestimos/gerenciar.html', context)

@login_required
@user_passes_test(is_staff_user)
def aprovar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    
    if request.method == 'POST':
        # Atualizar os status de empréstimo
        emprestimo.status = 'ativo'
        emprestimo.data_emprestimo = timezone.now()
        
        # Marcar o equipamento como indisponível
        emprestimo.equipamento.disponivel = False
        emprestimo.equipamento.save()
        
        emprestimo.save()
        messages.success(request, f'Empréstimo de {emprestimo.equipamento.nome} aprovado!')
    
    return redirect('gerenciar_emprestimos')

@login_required
@user_passes_test(is_staff_user)
def negar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    
    if request.method == 'POST':
        # Atualizar status para negado
        emprestimo.status = 'negado'
        emprestimo.save()
        messages.warning(request, f'Empréstimo de {emprestimo.equipamento.nome} negado.')
    
    return redirect('gerenciar_emprestimos')

@login_required
@user_passes_test(is_staff_user)
def finalizar_emprestimo(request, emprestimo_id):
    emprestimo = get_object_or_404(Emprestimo, id=emprestimo_id)
    
    if request.method == 'POST':
        # Atualizar status para finalizado
        emprestimo.status = 'finalizado'
        emprestimo.data_devolucao_real = timezone.now()
        
        # Marcar equipamento como disponível novamente
        emprestimo.equipamento.disponivel = True
        emprestimo.equipamento.save()
        
        emprestimo.save()
        messages.info(request, f'Empréstimo de {emprestimo.equipamento.nome} finalizado.')
    
    return redirect('gerenciar_emprestimos')