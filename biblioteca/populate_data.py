"""
Script para popular o banco de dados com dados de exemplo
Execute: python manage.py shell < populate_data.py
"""

from django.contrib.auth.models import User, Group
from catalogo.models import Autor, Livro, Emprestimo
from datetime import date, timedelta

# Criar grupos
leitores, _ = Group.objects.get_or_create(name='leitores')
bibliotecarios, _ = Group.objects.get_or_create(name='bibliotecarios')

# Criar usuários de exemplo
if not User.objects.filter(username='leitor1').exists():
    leitor = User.objects.create_user(
        username='leitor1',
        email='leitor1@example.com',
        password='senha123'
    )
    leitor.groups.add(leitores)
    print('✅ Usuário leitor1 criado (senha: senha123)')

if not User.objects.filter(username='bibliotecario1').exists():
    bib = User.objects.create_user(
        username='bibliotecario1',
        email='bib1@example.com',
        password='senha123'
    )
    bib.groups.add(bibliotecarios)
    print('✅ Usuário bibliotecario1 criado (senha: senha123)')

# Criar autores
autores_data = [
    {'nome': 'Machado de Assis', 'bio': 'Um dos maiores escritores brasileiros, conhecido por obras como Dom Casmurro e Memórias Póstumas de Brás Cubas.'},
    {'nome': 'Clarice Lispector', 'bio': 'Escritora brasileira naturalizada ucraniana, conhecida por sua prosa intimista e inovadora.'},
    {'nome': 'Jorge Amado', 'bio': 'Escritor baiano, conhecido por retratar a cultura e o povo da Bahia em suas obras.'},
    {'nome': 'Paulo Coelho', 'bio': 'Escritor brasileiro, um dos autores mais lidos no mundo.'},
    {'nome': 'Guimarães Rosa', 'bio': 'Escritor brasileiro, autor de Grande Sertão: Veredas.'},
]

autores = {}
for autor_data in autores_data:
    autor, created = Autor.objects.get_or_create(
        nome=autor_data['nome'],
        defaults={'bio': autor_data['bio']}
    )
    autores[autor.nome] = autor
    if created:
        print(f'✅ Autor {autor.nome} criado')

# Criar livros
livros_data = [
    {
        'titulo': 'Dom Casmurro',
        'autor': 'Machado de Assis',
        'categoria': 'romance',
        'ano_publicacao': 1899,
        'isbn': '978-8535911664',
        'sinopse': 'A história de Bentinho e Capitu, um dos maiores romances da literatura brasileira.',
        'editora': 'Companhia das Letras',
        'disponibilidade': True
    },
    {
        'titulo': 'A Hora da Estrela',
        'autor': 'Clarice Lispector',
        'categoria': 'ficcao',
        'ano_publicacao': 1977,
        'isbn': '978-8520925683',
        'sinopse': 'A história de Macabéa, uma nordestina que vive no Rio de Janeiro.',
        'editora': 'Rocco',
        'disponibilidade': True
    },
    {
        'titulo': 'Capitães da Areia',
        'autor': 'Jorge Amado',
        'categoria': 'ficcao',
        'ano_publicacao': 1937,
        'isbn': '978-8535914006',
        'sinopse': 'A vida de um grupo de meninos de rua em Salvador.',
        'editora': 'Companhia das Letras',
        'disponibilidade': True
    },
    {
        'titulo': 'O Alquimista',
        'autor': 'Paulo Coelho',
        'categoria': 'ficcao',
        'ano_publicacao': 1988,
        'isbn': '978-8522002726',
        'sinopse': 'A jornada de Santiago em busca de seu tesouro pessoal.',
        'editora': 'HarperCollins',
        'disponibilidade': True  # Será marcado como False ao criar o empréstimo
    },
    {
        'titulo': 'Grande Sertão: Veredas',
        'autor': 'Guimarães Rosa',
        'categoria': 'ficcao',
        'ano_publicacao': 1956,
        'isbn': '978-8520923306',
        'sinopse': 'O relato de Riobaldo sobre sua vida no sertão.',
        'editora': 'Nova Fronteira',
        'disponibilidade': True
    },
    {
        'titulo': 'Memórias Póstumas de Brás Cubas',
        'autor': 'Machado de Assis',
        'categoria': 'romance',
        'ano_publicacao': 1881,
        'isbn': '978-8535911657',
        'sinopse': 'As memórias de um defunto autor que narra sua própria vida.',
        'editora': 'Companhia das Letras',
        'disponibilidade': True
    },
]

for livro_data in livros_data:
    autor_nome = livro_data.pop('autor')
    livro, created = Livro.objects.get_or_create(
        isbn=livro_data['isbn'],
        defaults={**livro_data, 'autor': autores[autor_nome]}
    )
    if created:
        print(f'✅ Livro "{livro.titulo}" criado')

# Criar um empréstimo de exemplo (O Alquimista emprestado)
if User.objects.filter(username='leitor1').exists():
    leitor = User.objects.get(username='leitor1')
    livro = Livro.objects.get(titulo='O Alquimista')

    if not Emprestimo.objects.filter(livro=livro, usuario=leitor, status='ativo').exists():
        emprestimo = Emprestimo.objects.create(
            livro=livro,
            usuario=leitor,
            data_fim_prevista=date.today() + timedelta(days=14)
        )
        print(f'✅ Empréstimo de "{livro.titulo}" criado para {leitor.username}')

print('\n🎉 Banco de dados populado com sucesso!')
print('\n📋 Usuários criados:')
print('   - leitor1 / senha123 (grupo: leitores)')
print('   - bibliotecario1 / senha123 (grupo: bibliotecarios)')
print(f'\n📚 Total de livros: {Livro.objects.count()}')
print(f'👤 Total de autores: {Autor.objects.count()}')
print(f'📖 Total de empréstimos: {Emprestimo.objects.count()}')
