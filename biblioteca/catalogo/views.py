from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from .models import Livro, Autor, Emprestimo
from .forms import LivroForm, AutorForm, EmprestimoForm


def is_bibliotecario(user):
    """Verifica se o usuário pertence ao grupo bibliotecarios"""
    return user.groups.filter(name='bibliotecarios').exists()


def bibliotecario_required(view_func):
    """Decorator que verifica se o usuário é bibliotecário"""
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('contas:login')
        if not is_bibliotecario(request.user):
            messages.error(request, 'Você não tem permissão para acessar esta página. Apenas bibliotecários podem realizar esta ação.')
            return redirect('catalogo:home')
        return view_func(request, *args, **kwargs)
    return wrapper


def home(request):
    """Página inicial - acessível a todos"""
    livros_recentes = Livro.objects.all()[:6]
    context = {
        'livros_recentes': livros_recentes,
    }
    return render(request, 'catalogo/home.html', context)


@login_required
def livros_list(request):
    """Lista todos os livros"""
    livros = Livro.objects.select_related('autor').all()
    categoria_filtro = request.GET.get('categoria')
    disponivel_filtro = request.GET.get('disponivel')

    if categoria_filtro:
        livros = livros.filter(categoria=categoria_filtro)

    if disponivel_filtro == 'sim':
        livros = livros.filter(disponibilidade=True)
    elif disponivel_filtro == 'nao':
        livros = livros.filter(disponibilidade=False)

    context = {
        'livros': livros,
        'categorias': Livro.CATEGORIAS,
    }
    return render(request, 'catalogo/livros_list.html', context)


@login_required
def livro_detail(request, pk):
    """Detalhes de um livro"""
    livro = get_object_or_404(Livro, pk=pk)
    context = {
        'livro': livro,
        'is_bibliotecario': is_bibliotecario(request.user),
    }
    return render(request, 'catalogo/livro_detail.html', context)


@login_required
@bibliotecario_required
def livro_create(request):
    """Criar novo livro - apenas bibliotecários"""
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro cadastrado com sucesso!')
            return redirect('catalogo:livros_list')
    else:
        form = LivroForm()

    context = {'form': form, 'titulo': 'Cadastrar Livro'}
    return render(request, 'catalogo/livro_form.html', context)


@login_required
@bibliotecario_required
def livro_edit(request, pk):
    """Editar livro - apenas bibliotecários"""
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect('catalogo:livro_detail', pk=pk)
    else:
        form = LivroForm(instance=livro)

    context = {'form': form, 'titulo': 'Editar Livro', 'livro': livro}
    return render(request, 'catalogo/livro_form.html', context)


@login_required
@bibliotecario_required
def livro_delete(request, pk):
    """Excluir livro - apenas bibliotecários"""
    livro = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('catalogo:livros_list')

    context = {'livro': livro}
    return render(request, 'catalogo/livro_confirm_delete.html', context)


@login_required
def emprestimo_create(request):
    """Criar empréstimo - leitores e bibliotecários"""
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            emprestimo.usuario = request.user
            emprestimo.save()
            messages.success(request, f'Empréstimo do livro "{emprestimo.livro.titulo}" realizado com sucesso!')
            return redirect('catalogo:meus_emprestimos')
    else:
        form = EmprestimoForm()

    context = {'form': form}
    return render(request, 'catalogo/emprestimo_form.html', context)


@login_required
def meus_emprestimos(request):
    """Lista empréstimos do usuário logado"""
    emprestimos = Emprestimo.objects.filter(usuario=request.user).select_related('livro', 'livro__autor')
    context = {'emprestimos': emprestimos}
    return render(request, 'catalogo/meus_emprestimos.html', context)


@login_required
def emprestimo_finalizar(request, pk):
    """Finalizar empréstimo - próprio usuário ou bibliotecário"""
    emprestimo = get_object_or_404(Emprestimo, pk=pk)

    # Verificar permissão
    if emprestimo.usuario != request.user and not is_bibliotecario(request.user):
        raise PermissionDenied

    if request.method == 'POST':
        emprestimo.finalizar()
        messages.success(request, 'Empréstimo finalizado com sucesso!')
        return redirect('catalogo:meus_emprestimos')

    context = {'emprestimo': emprestimo}
    return render(request, 'catalogo/emprestimo_confirm_finalizar.html', context)


@login_required
@bibliotecario_required
def todos_emprestimos(request):
    """Lista todos os empréstimos - apenas bibliotecários"""
    emprestimos = Emprestimo.objects.select_related('livro', 'livro__autor', 'usuario').all()
    status_filtro = request.GET.get('status')

    if status_filtro:
        emprestimos = emprestimos.filter(status=status_filtro)

    context = {
        'emprestimos': emprestimos,
        'status_choices': Emprestimo.STATUS_CHOICES,
    }
    return render(request, 'catalogo/todos_emprestimos.html', context)


@login_required
@bibliotecario_required
def autor_create(request):
    """Criar autor - apenas bibliotecários"""
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor cadastrado com sucesso!')
            return redirect('catalogo:livro_create')
    else:
        form = AutorForm()

    context = {'form': form}
    return render(request, 'catalogo/autor_form.html', context)
