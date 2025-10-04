from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Livros
    path('livros/', views.livros_list, name='livros_list'),
    path('livros/<int:pk>/', views.livro_detail, name='livro_detail'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/<int:pk>/editar/', views.livro_edit, name='livro_edit'),
    path('livros/<int:pk>/excluir/', views.livro_delete, name='livro_delete'),

    # Autores
    path('autores/novo/', views.autor_create, name='autor_create'),

    # Empréstimos
    path('emprestimos/novo/', views.emprestimo_create, name='emprestimo_create'),
    path('emprestimos/meus/', views.meus_emprestimos, name='meus_emprestimos'),
    path('emprestimos/<int:pk>/finalizar/', views.emprestimo_finalizar, name='emprestimo_finalizar'),
    path('emprestimos/todos/', views.todos_emprestimos, name='todos_emprestimos'),
]
