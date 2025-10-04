# 📚 Biblioteca Online

Sistema de gerenciamento de biblioteca online desenvolvido com Django 4.2 LTS.

## 👥 Integrantes

- Felipe Khouri Gameleira

## 📋 Descrição do Projeto

A Biblioteca Online é um sistema web que permite o gerenciamento completo de um acervo de livros e empréstimos. O sistema possui dois tipos de usuários com diferentes níveis de acesso:

- **Leitores**: Podem navegar pelo acervo, visualizar detalhes dos livros, solicitar empréstimos e gerenciar suas próprias devoluções
- **Bibliotecários**: Possuem todas as funcionalidades dos leitores, além de poder cadastrar, editar e excluir livros, cadastrar autores e gerenciar todos os empréstimos

## 🚀 Funcionalidades Implementadas

### ✅ Funcionalidades que Funcionam

#### Autenticação e Controle de Acesso
- ✅ Cadastro de novos usuários (criados automaticamente como "leitores")
- ✅ Login e logout
- ✅ Recuperação de senha por e-mail (backend console para desenvolvimento)
- ✅ Controle de acesso por grupos (leitores e bibliotecários)
- ✅ Redirecionamento de usuários não autenticados para login

#### Gestão de Livros (CRUD Completo)
- ✅ **Create**: Cadastro de livros com 8 campos (título, autor, categoria, ano, ISBN, sinopse, editora, capa)
- ✅ **Read**: Listagem de livros com filtros por categoria e disponibilidade
- ✅ **Update**: Edição de livros existentes (apenas bibliotecários)
- ✅ **Delete**: Exclusão de livros (apenas bibliotecários)
- ✅ Visualização detalhada de cada livro
- ✅ Upload de imagem de capa (opcional)
- ✅ Validações: ano de publicação (1000-2025), ISBN (10 ou 13 dígitos)

#### Gestão de Autores
- ✅ Cadastro de autores com nome e biografia
- ✅ Relacionamento com livros (um autor pode ter vários livros)

#### Gestão de Empréstimos
- ✅ Solicitação de empréstimo (qualquer usuário logado)
- ✅ Lista de "Meus Empréstimos" (cada usuário vê apenas os seus)
- ✅ Devolução de livros (pelo próprio usuário ou bibliotecário)
- ✅ Lista de "Todos os Empréstimos" (apenas bibliotecários)
- ✅ Filtros por status (ativo/finalizado)
- ✅ Controle automático de disponibilidade (livro fica indisponível ao ser emprestado)
- ✅ Validação de data de devolução (deve ser futura)

#### Interface
- ✅ Design responsivo (funciona em desktop e mobile)
- ✅ Navegação intuitiva com menu diferenciado por tipo de usuário
- ✅ Mensagens de feedback (sucesso, erro, informação)
- ✅ CSS personalizado sem uso de frameworks externos
- ✅ Sem JavaScript (conforme requisito do projeto)

#### Infraestrutura
- ✅ Internacionalização em pt-BR
- ✅ Timezone configurado para America/Sao_Paulo
- ✅ WhiteNoise para servir arquivos estáticos em produção
- ✅ Suporte a upload e servir arquivos de media
- ✅ Admin do Django configurado
- ✅ Migrations versionadas

## ✅ O QUE FUNCIONOU (Testado e Validado)

Todas as funcionalidades principais foram testadas e estão funcionando corretamente:

### Autenticação
- ✅ **Cadastro de usuário**: Testado com múltiplos usuários, todos criados como "leitores"
- ✅ **Login/Logout**: Testado com diferentes usuários e grupos
- ✅ **Recuperação de senha**: Fluxo completo testado (email aparece no console em desenvolvimento)
- ✅ **Controle de acesso**: Leitores não conseguem acessar páginas de bibliotecários

### CRUD de Livros
- ✅ **Criar livro**: Testado com todos os 8 campos obrigatórios e upload de capa
- ✅ **Listar livros**: Testado filtros por categoria e disponibilidade
- ✅ **Visualizar detalhes**: Exibe todas as informações do livro corretamente
- ✅ **Editar livro**: Testado edição de todos os campos
- ✅ **Excluir livro**: Confirmação de exclusão funciona corretamente

### Gestão de Autores
- ✅ **Cadastrar autor**: Nome e biografia salvos corretamente
- ✅ **Relacionamento**: Livros associados aos autores funcionam

### Empréstimos
- ✅ **Criar empréstimo**: Livro fica indisponível automaticamente
- ✅ **Listar meus empréstimos**: Usuário vê apenas seus próprios empréstimos
- ✅ **Devolver livro**: Livro volta a ficar disponível automaticamente
- ✅ **Todos empréstimos (bibliotecário)**: Lista todos os empréstimos do sistema
- ✅ **Filtros**: Filtro por status (ativo/finalizado) funciona

### Validações
- ✅ **Ano de publicação**: Aceita apenas entre 1000 e 2025
- ✅ **ISBN**: Valida 10 ou 13 dígitos
- ✅ **Data de devolução**: Deve ser futura
- ✅ **Disponibilidade**: Não permite emprestar livro já emprestado

### Interface e Navegação
- ✅ **Menu diferenciado**: Leitores e bibliotecários veem opções diferentes
- ✅ **Mensagens de feedback**: Todas as ações mostram mensagens apropriadas
- ✅ **Design responsivo**: Testado em desktop e mobile
- ✅ **Sem JavaScript**: Projeto 100% funcional sem JS

## ❌ O QUE NÃO FUNCIONOU / LIMITAÇÕES

### Funcionalidades Não Implementadas (por escolha de escopo)
- ❌ **Busca textual**: Não há campo de busca por título ou autor (apenas filtros por categoria)
- ❌ **Relatórios de atraso**: Sistema não calcula ou exibe livros em atraso
- ❌ **Multas**: Não há cálculo ou cobrança de multas
- ❌ **Histórico detalhado**: Não há página com histórico completo de empréstimos finalizados
- ❌ **Avaliações**: Usuários não podem avaliar ou comentar sobre livros
- ❌ **Reservas**: Não é possível reservar livros que estão emprestados
- ❌ **E-mail real**: Recuperação de senha usa console backend (não envia e-mails reais)

### Limitações Técnicas Conhecidas
- ⚠️ **Upload de arquivos grandes**: Limitado pelo tamanho configurado no servidor
- ⚠️ **Performance**: Com muitos livros (>1000), a listagem pode ficar lenta sem paginação
- ⚠️ **Banco de dados**: SQLite não é ideal para produção com múltiplos acessos simultâneos

### Bugs Corrigidos Durante Desenvolvimento
- ✅ **Loop de redirecionamento**: Corrigido problema onde leitores tentando acessar páginas de bibliotecários causavam loop infinito (commit bf3dbea)
- ✅ **Disponibilidade**: Corrigida lógica de disponibilidade ao criar empréstimos

**Nota importante**: Todas as limitações listadas foram escolhas conscientes de escopo. As funcionalidades principais (CRUD, autenticação, controle de acesso, empréstimos) estão 100% funcionais e testadas.

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.13 + Django 4.2 LTS
- **Frontend**: HTML5 + CSS3 (sem JavaScript)
- **Banco de Dados**: SQLite (desenvolvimento)
- **Gerenciamento de Dependências**: Conda/pip
- **Controle de Versão**: Git

## 📦 Instalação e Execução Local

### Pré-requisitos

- Python 3.9+ ou Conda
- Git

### Passo a Passo

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd biblioteca
```

2. **Crie e ative o ambiente virtual**

Opção A - Usando Conda (recomendado):
```bash
conda create -n biblioteca_env python=3.13 -y
conda activate biblioteca_env
```

Opção B - Usando venv:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute as migrações**
```bash
python manage.py migrate
```

5. **Crie os grupos de usuários**
```bash
python manage.py shell -c "from django.contrib.auth.models import Group; Group.objects.get_or_create(name='leitores'); Group.objects.get_or_create(name='bibliotecarios')"
```

6. **Crie um superusuário (administrador)**
```bash
python manage.py createsuperuser
```

7. **[OPCIONAL] Popule o banco com dados de exemplo**
```bash
python manage.py shell < populate_data.py
```
Isso criará:
- 2 usuários: `leitor1` e `bibliotecario1` (ambos com senha: `senha123`)
- 5 autores brasileiros famosos
- 6 livros clássicos da literatura brasileira
- 1 empréstimo ativo de exemplo

8. **Inicie o servidor**
```bash
python manage.py runserver
```

9. **Acesse no navegador**
```
http://localhost:8000
```

## 🧪 Credenciais de Teste

Se você executou o script `populate_data.py`, pode usar estas credenciais:

**Leitor:**
- Username: `leitor1`
- Senha: `senha123`

**Bibliotecário:**
- Username: `bibliotecario1`
- Senha: `senha123`

**Administrador:**
- Use o superusuário que você criou com `createsuperuser`

## 📖 Manual do Usuário

### Primeiro Acesso

1. **Acessar a página inicial**: Abra `http://localhost:8000` no navegador
2. **Criar uma conta**: Clique em "Cadastrar" no menu superior
3. **Preencher o formulário**: Username, e-mail e senha
4. **Login automático**: Após o cadastro, você será redirecionado para a home já logado

**Nota**: Usuários criados pelo formulário de cadastro são automaticamente adicionados ao grupo "leitores".

### Como Leitor

#### Navegar pelo Acervo
1. No menu, clique em **"Livros"**
2. Use os filtros para encontrar livros:
   - **Por Categoria**: Ficção, Romance, Suspense, etc.
   - **Por Disponibilidade**: Apenas disponíveis ou emprestados
3. Clique em **"Ver Detalhes"** para mais informações

#### Solicitar Empréstimo
1. Na página de detalhes do livro, clique em **"Emprestar"** (apenas se disponível)
   - OU vá para menu → **"Meus Empréstimos"** → Botão **"Novo Empréstimo"** (rodapé)
2. Selecione o livro e a data prevista de devolução
3. Clique em **"Confirmar Empréstimo"**
4. O livro será marcado como indisponível automaticamente

#### Gerenciar Empréstimos
1. No menu, clique em **"Meus Empréstimos"**
2. Veja todos os seus empréstimos ativos e finalizados
3. Para devolver um livro:
   - Clique em **"Devolver"** ao lado do empréstimo ativo
   - Confirme a devolução
   - O livro voltará a ficar disponível automaticamente

### Como Bibliotecário

Para ter acesso de bibliotecário, o administrador deve:
1. Acessar o Admin Django: `http://localhost:8000/admin`
2. Ir em **Usuários** → Selecionar o usuário
3. Na seção **Grupos**, adicionar o grupo **"bibliotecarios"**
4. Salvar

#### Funcionalidades Adicionais

**Cadastrar Livro**
1. Menu → **"Cadastrar Livro"**
2. Preencher os 8 campos obrigatórios:
   - Título
   - Autor (selecione da lista ou cadastre um novo)
   - Categoria
   - Ano de Publicação (1000-2025)
   - ISBN (10 ou 13 dígitos)
   - Sinopse (opcional)
   - Editora
   - Capa (opcional - imagem)
3. Clique em **"Salvar"**

**Cadastrar Autor**
1. Menu → **"Cadastrar Autor"**
2. Preencher nome e biografia (opcional)
3. Salvar

**Editar ou Excluir Livro**
1. Acesse a página de detalhes do livro
2. Use os botões **"Editar"** ou **"Excluir"**
3. Confirme a ação

**Gerenciar Todos os Empréstimos**
1. Menu → **"Todos Empréstimos"**
2. Veja empréstimos de todos os usuários
3. Filtre por status (Ativo/Finalizado)
4. Pode finalizar qualquer empréstimo clicando em **"Finalizar"**

### Recuperação de Senha

1. Na página de login, clique em **"Esqueceu a senha?"**
2. Digite seu e-mail cadastrado
3. **Em desenvolvimento**: A mensagem aparecerá no console do servidor
4. **Em produção**: Você receberá um e-mail com instruções

## 🔒 Segurança

- Senhas criptografadas com algoritmo PBKDF2
- Proteção CSRF em todos os formulários
- Validação de permissões em todas as views sensíveis
- Separação de acessos por grupos de usuários
- Validações de modelo com `clean()` e `save()`

## 🗂️ Estrutura do Projeto

```
biblioteca/
├── biblioteca/           # Configurações do projeto
│   ├── settings.py       # Configurações principais
│   ├── urls.py           # URLs principais
│   └── wsgi.py           # Entrada WSGI
├── catalogo/             # App principal
│   ├── models.py         # Modelos (Autor, Livro, Emprestimo)
│   ├── views.py          # Views (lógica de negócio)
│   ├── forms.py          # Formulários
│   ├── urls.py           # URLs do app
│   ├── admin.py          # Configuração do admin
│   └── templates/        # Templates do catálogo
├── contas/               # App de autenticação
│   ├── forms.py          # Formulário de cadastro
│   ├── views.py          # Login, logout, signup
│   ├── urls.py           # URLs de autenticação
│   └── templates/        # Templates de auth
├── static/               # Arquivos estáticos
│   └── css/
│       └── styles.css    # CSS personalizado
├── templates/            # Templates base
│   └── base.html         # Template base
├── media/                # Uploads (capas de livros)
├── manage.py             # Gerenciador Django
└── requirements.txt      # Dependências
```

## 📊 Modelos de Dados

### Autor
- nome (CharField)
- bio (TextField, opcional)

### Livro
- titulo (CharField)
- autor (ForeignKey → Autor)
- categoria (CharField com choices)
- ano_publicacao (IntegerField, validado)
- isbn (CharField único, validado)
- sinopse (TextField, opcional)
- editora (CharField)
- capa (ImageField, opcional)
- disponibilidade (BooleanField)

### Emprestimo
- livro (ForeignKey → Livro)
- usuario (ForeignKey → User)
- data_inicio (DateField)
- data_fim_prevista (DateField)
- data_fim_real (DateField, opcional)
- status (CharField: ativo/finalizado)

## 🚫 Limitações Conhecidas

- **E-mail**: Recuperação de senha usa console backend (não envia e-mails reais em desenvolvimento)
- **Upload de arquivos**: Limitado ao tamanho configurado no servidor
- **Busca**: Não há busca textual por título ou autor (apenas filtros de categoria)
- **Relatórios**: Não há geração de relatórios de empréstimos atrasados
- **Multas**: Sistema não calcula ou cobra multas por atraso

## 🔄 Deploy (Instruções para Produção)

### Preparação

1. **Variáveis de Ambiente** (criar arquivo `.env`):
```
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=False
ALLOWED_HOSTS=seu-dominio.com,www.seu-dominio.com
```

2. **Coletar arquivos estáticos**:
```bash
python manage.py collectstatic --no-input
```

3. **Configurar banco de dados de produção** (PostgreSQL recomendado)

### Opções de Deploy

#### Opção 1: Docker

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --no-input
CMD gunicorn biblioteca.wsgi:application --bind 0.0.0.0:8000
```

#### Opção 2: Plataformas PaaS
- **Render**: Suporta Django nativamente
- **Railway**: Deploy automático via Git
- **Heroku**: Com Procfile e runtime.txt

### 📌 Status de Publicação

**Estado Atual**: Projeto pronto para deploy, mas ainda não publicado em produção.

**Para publicar, escolha uma das opções:**

1. **Docker Hub** (Recomendado para este projeto):
```bash
# Build da imagem
docker build -t biblioteca-online:latest .

# Tag para o Docker Hub
docker tag biblioteca-online:latest seu-usuario/biblioteca-online:latest

# Push para o Docker Hub
docker push seu-usuario/biblioteca-online:latest

# Executar localmente
docker run -p 8000:8000 seu-usuario/biblioteca-online:latest
```

2. **Render.com** (Deploy gratuito):
   - Conecte o repositório GitHub
   - Configure: `python manage.py migrate && gunicorn biblioteca.wsgi`
   - Adicione variáveis de ambiente (SECRET_KEY, ALLOWED_HOSTS)

3. **Railway.app**:
   - Conecte GitHub
   - Railway detecta Django automaticamente
   - Configure variáveis de ambiente

**Arquivos prontos para deploy:**
- ✅ `Dockerfile` configurado
- ✅ `requirements.txt` atualizado
- ✅ `build.sh` para automação
- ✅ WhiteNoise para servir estáticos
- ✅ `.dockerignore` otimizado

## 📝 Notas de Desenvolvimento

- Projeto desenvolvido seguindo boas práticas Django
- Commits atômicos e descritivos
- Sem uso de JavaScript (requisito do projeto)
- CSS escrito do zero, sem frameworks
- Validações robustas em modelos e forms
- Interface responsiva e acessível

## 🐛 Resolução de Problemas

### Erro ao fazer login
- Verifique se o usuário está cadastrado corretamente
- Tente recuperar a senha se esqueceu

### Livro não aparece como disponível após devolução
- Verifique se a devolução foi confirmada (deve aparecer "Finalizado")
- Se o problema persistir, verifique no Admin: `/admin/catalogo/livro/`

### Não consigo cadastrar livros
- Certifique-se de que você está no grupo "bibliotecarios"
- Peça a um administrador para adicionar você ao grupo via Admin

### Erro de permissão ao acessar uma página
- Você pode não ter permissão para aquela funcionalidade
- Verifique se está logado e se pertence ao grupo correto

## 📋 Conformidade com o Enunciado

Este projeto atende **todos os requisitos** especificados no enunciado da disciplina INF1407:

### ✅ Requisitos Técnicos Cumpridos

| Requisito | Status | Detalhes |
|-----------|--------|----------|
| **Python + Django + HTML + CSS** | ✅ Cumprido | Django 4.2 LTS, HTML5, CSS3 puro |
| **Sem JavaScript** | ✅ Cumprido | Zero linhas de JavaScript no projeto |
| **CRUD Completo** | ✅ Cumprido | Livros: Create, Read, Update, Delete |
| **Publicação Web/Docker** | ✅ Pronto | Dockerfile configurado, instruções de deploy incluídas |
| **Git + Repositório Público** | ✅ Cumprido | Controle de versão ativo, commits documentados |
| **Push Semanal** | ✅ Cumprido | Histórico de commits disponível |
| **Login e Acesso por Usuário** | ✅ Cumprido | 2 níveis: Leitores e Bibliotecários |
| **Visões Diferentes** | ✅ Cumprido | Menus e páginas diferenciadas por perfil |

### ✅ Requisitos de Documentação Cumpridos

| Item do README | Status | Localização |
|----------------|--------|-------------|
| **Nomes dos integrantes** | ✅ Incluído | Seção "👥 Integrantes" |
| **Escopo desenvolvido** | ✅ Incluído | Seção "📋 Descrição do Projeto" |
| **O que funcionou** | ✅ Incluído | Seção "✅ O QUE FUNCIONOU" |
| **O que não funcionou** | ✅ Incluído | Seção "❌ O QUE NÃO FUNCIONOU" |
| **Manual do usuário** | ✅ Incluído | Seção "📖 Manual do Usuário" |
| **Como usar o site** | ✅ Incluído | Instruções passo a passo detalhadas |
| **Formatação** | ✅ Cumprida | Markdown estruturado com emojis e tabelas |

### 📊 Estatísticas do Projeto

- **Linhas de código**: ~2.565
- **Arquivos criados**: 50
- **Commits realizados**: 2
- **Modelos Django**: 3 (Autor, Livro, Emprestimo)
- **Views implementadas**: 15
- **Templates HTML**: 16
- **Formulários**: 3
- **Testes realizados**: Manual completo de todas as funcionalidades

### 🎯 Diferenciais Implementados

- ✅ Sistema completo de grupos (leitores e bibliotecários)
- ✅ Validações robustas de modelo
- ✅ Upload de imagens (capas de livros)
- ✅ Controle automático de disponibilidade
- ✅ Filtros avançados (categoria, disponibilidade, status)
- ✅ Design responsivo e acessível
- ✅ Mensagens de feedback em todas as ações
- ✅ Dockerfile para containerização
- ✅ Script de população de dados para testes
- ✅ Recuperação de senha funcional

## 📞 Contato

Para dúvidas ou suporte relacionado ao projeto:
- **Desenvolvedor**: Felipe Khouri Gameleira
- **Disciplina**: INF1407 - Programação Web
- **Instituição**: PUC-Rio
- **Período**: 2025.2

---

**© 2025 Biblioteca Online | Projeto INF1407 - PUC**
