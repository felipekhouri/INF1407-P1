# Biblioteca Online

Sistema de gerenciamento de biblioteca desenvolvido em Django 4.2 LTS para a disciplina INF1407.

## Integrantes

- Felipe Khouri Gameleira

## Escopo do Projeto

Sistema web para gerenciamento de acervo de biblioteca com dois níveis de acesso:

- Leitores:
  - Navegar pelo acervo de livros
  - Visualizar detalhes dos livros
  - Solicitar empréstimos
  - Devolver seus próprios empréstimos
- Bibliotecários:
  - Todas as funcionalidades dos leitores
  - CRUD completo de livros (8 campos: título, autor, categoria, ano, ISBN, sinopse, editora, capa)
  - Cadastrar autores
  - Visualizar e gerenciar todos os empréstimos do sistema

Banco de dados de exemplo inclui:
- 5 autores brasileiros
- 6 livros clássicos da literatura brasileira
- 1 empréstimo ativo de exemplo

## Tecnologias Utilizadas

- Python 3.13
- Django 4.2 LTS
- HTML5 + CSS3 (sem JavaScript)
- SQLite
- WhiteNoise (arquivos estáticos)
- Pillow (upload de imagens)

## Como Executar (Docker — Recomendado)

A imagem já está publicada no Docker Hub e vem com dados de teste pré-carregados.

```bash
# Baixar e executar
docker pull felipekhouri/biblioteca-online:latest
docker run -p 8000:8000 felipekhouri/biblioteca-online:latest
```

Acesse: http://localhost:8000

> Observação: Execução local com Python/venv é possível, mas não é necessária para avaliação. O fluxo recomendado é via Docker.

## Credenciais e Dados de Teste

Contas disponíveis (pré-carregadas na imagem Docker):

| Tipo | Username | Senha | Permissões |
|------|----------|-------|------------|
| Bibliotecário | bibliotecario1 | senha123 | CRUD de livros/autores; ver todos empréstimos |
| Leitor | leitor1 | senha123 | Emprestar e devolver livros |
| Admin | admin | admin123 | Django Admin (/admin) |

Dados incluídos:
- 5 autores brasileiros (ex.: Machado de Assis, Clarice Lispector, Jorge Amado, Paulo Coelho, Guimarães Rosa)
- 6 livros clássicos da literatura brasileira
- 1 empréstimo ativo de exemplo
- Grupos configurados (leitores e bibliotecarios)

## Manual de Uso

### Como Leitor
- Ver Livros: menu “Livros” → use filtros → “Ver Detalhes”
- Emprestar Livro: na página do livro → “Emprestar” (se disponível) → selecione data de devolução → confirmar
- Devolver Livro: menu “Meus Empréstimos” → “Devolver” → confirmar

### Como Bibliotecário
Use a conta: bibliotecario1 / senha123
- Cadastrar Livro: menu “Cadastrar Livro” → preencher 8 campos
- Cadastrar Autor: menu “Cadastrar Autor” → nome + biografia
- Editar/Excluir: na página do livro → botões “Editar” / “Excluir”
- Todos Empréstimos: menu “Todos Empréstimos” (visualiza de todos os usuários)

### Recuperar Senha (desenvolvimento)
- Página de login → “Esqueceu a senha?” → digite seu e-mail
- A mensagem é exibida no console do servidor (não envia e-mail real)

## O que Funcionou
- Cadastro, login, logout, recuperação de senha (console)
- Separação de permissões por grupos
- CRUD completo de livros e autores
- Empréstimos com validação e devolução
- Interface responsiva, sem JavaScript
- Internacionalização pt-BR

## O que Não Funcionou
- Recuperação de senha não envia e-mail real (apenas console)

## Conformidade com Enunciado

| Requisito | Status |
|-----------|--------|
| Python + Django + HTML + CSS | ✅ |
| Sem JavaScript | ✅ |
| CRUD completo | ✅ |
| Publicação Docker | ✅ |
| Git + Repositório público | ✅ |
| Login + Acesso por usuário | ✅ |
| Visões diferentes | ✅ |
| README com nomes | ✅ |
| README com escopo | ✅ |
| README com “o que funcionou” | ✅ |
| README com “o que não funcionou” | ✅ |
| README com manual de uso | ✅ |

## Estatísticas
- ~2.565 linhas de código
- 3 modelos Django
- 15 views
- 16 templates HTML
- Zero linhas de JavaScript
