from django.contrib import admin
from .models import Autor, Livro, Emprestimo


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'criado_em')
    search_fields = ('nome',)
    ordering = ('nome',)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'ano_publicacao', 'isbn', 'disponibilidade')
    list_filter = ('categoria', 'disponibilidade', 'autor')
    search_fields = ('titulo', 'isbn', 'autor__nome')
    ordering = ('-criado_em',)


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'usuario', 'data_inicio', 'data_fim_prevista', 'status')
    list_filter = ('status', 'data_inicio')
    search_fields = ('livro__titulo', 'usuario__username')
    ordering = ('-criado_em',)
