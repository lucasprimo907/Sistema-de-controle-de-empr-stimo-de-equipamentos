from django.shortcuts import render
from django.db.models import Q
from .models import Equipamento, Categoria

def home(request):
    total_equipamentos = Equipamento.objects.count()
    equipamentos_disponiveis = Equipamento.objects.filter(disponivel=True).count()
    total_categorias = Categoria.objects.count()
    
    print(f"DEBUG: Total equipamentos: {total_equipamentos}")
    print(f"DEBUG: Disponíveis: {equipamentos_disponiveis}") 
    print(f"DEBUG: Categorias: {total_categorias}")
    
    context = {
        'total_equipamentos': total_equipamentos,
        'equipamentos_disponiveis': equipamentos_disponiveis,
        'total_categorias': total_categorias,
    }
    return render(request, 'home.html', context)

def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    equipamentos_disponiveis_count = Equipamento.objects.filter(disponivel=True).count()
    categorias_count = Categoria.objects.count()
    
    context = {
        'equipamentos': equipamentos,
        'equipamentos_disponiveis_count': equipamentos_disponiveis_count,
        'categorias_count': categorias_count,
    }
    return render(request, 'equipamentos/lista.html', context)

def buscar_equipamentos(request):
    query = request.GET.get('q', '')
    categoria_id = request.GET.get('categoria', '')
    somente_disponiveis = request.GET.get('disponiveis', False)
    
    equipamentos = Equipamento.objects.all()
    
    # Aplicar filtros
    if query:
        equipamentos = equipamentos.filter(
            Q(nome__icontains=query) |
            Q(numero_serie__icontains=query) |
            Q(descricao__icontains=query) |
            Q(categoria__nome__icontains=query)
        )
    
    if categoria_id:
        equipamentos = equipamentos.filter(categoria_id=categoria_id)
    
    if somente_disponiveis:
        equipamentos = equipamentos.filter(disponivel=True)
    
    categorias = Categoria.objects.all()
    
    context = {
        'equipamentos': equipamentos,
        'query': query,
        'categoria_selecionada': categoria_id,
        'somente_disponiveis': somente_disponiveis,
        'categorias': categorias,
        'total_resultados': equipamentos.count(),
    }
    return render(request, 'equipamentos/busca.html', context)