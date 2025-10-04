# 📚 Biblioteca Online

Sistema de gerenciamento de biblioteca desenvolvido em Django 4.2 LTS para a disciplina INF1407.

## 👥 Integrantes

- Felipe Khouri Gameleira

---

## 📋 Escopo do Proje- 5 autores brasileiros (Machado de Assis, Clarice Lispector, etc.)
- 6 livros clássicos da lit## 📋 Conformidade com Enunciado

| Requisito | Status |
|-----------|--------|
| Python + Django + HTML + CSS | ✅ |
| **Sem JavaScript** | ✅ |
| CRUD completo | ✅ |
| **Publicação Docker** | ✅ **PUBLICADO** |
| Git + Repositório público | ✅ |
| Login + Acesso por usuário | ✅ |
| Visões diferentes | ✅ |
| README com nomes | ✅ |
| README com escopo | ✅ |
| README com "o que funcionou" | ✅ |
| README com "o que não funcionou" | ✅ |
| README com manual de uso | ✅ |

**Links de Entrega**:
- 🐳 **Docker Hub**: https://hub.docker.com/r/felipekhouri/biblioteca-online
- 📦 **GitHub**: https://github.com/felipekhouri/INF1407-P1

**Estatísticas**:
- 1 empréstimo ativo de exemplo

---

## 🐳 Executar com Docker

### ✅ Imagem Publicada no Docker Hub

**Link da imagem**: https://hub.docker.com/r/felipekhouri/biblioteca-online

### Método 1: Usar imagem pronta (Recomendado)

```bash
# Baixar e executar a imagem
docker pull felipekhouri/biblioteca-online:latest
docker run -p 8000:8000 felipekhouri/biblioteca-online:latest
```

Acesse: `http://localhost:8000`

**Criar um superusuário no container**:
```bash
# Descubra o ID do container
docker ps

# Execute o comando dentro do container
docker exec -it <container_id> python manage.py createsuperuser
```

**Popular com dados de teste**:
```bash
docker exec -it <container_id> python manage.py shell < populate_data.py
```

### Método 2: Build local

```bash
git clone https://github.com/felipekhouri/INF1407-P1.git
cd INF1407-P1/biblioteca
docker build -t biblioteca-online .
docker run -p 8000:8000 biblioteca-online
```

---

## 🌐 Outras Opções de Deploy

### Render.com (Grátis)
1. Conecte repositório GitHub
2. Build: `pip install -r requirements.txt && python manage.py migrate`
3. Start: `gunicorn biblioteca.wsgi`
4. Variáveis: `SECRET_KEY`, `ALLOWED_HOSTS`, `DEBUG=False`

### Railway
1. Conecte GitHub
2. Railway detecta Django automaticamente
3. Configure variáveis de ambiente

**Arquivos incluídos**: `Dockerfile`, `build.sh`, `requirements.txt`, `.dockerignore`
Sistema web para gerenciamento de acervo de biblioteca com **dois níveis de acesso**:

### 👤 Leitores
- Navegar pelo acervo de livros
- Visualizar detalhes dos livros
- Solicitar empréstimos
- Gerenciar devoluções de seus próprios empréstimos

### 👨‍💼 Bibliotecários
- Todas as funcionalidades dos leitores +
- **CRUD completo de livros** (8 campos: título, autor, categoria, ano, ISBN, sinopse, editora, capa)
- Cadastrar autores
- Visualizar e gerenciar todos os empréstimos do sistema

---

## ✅ O QUE FUNCIONOU (Testado e Validado)

### Autenticação e Controle de Acesso
- ✅ Cadastro de usuários (automaticamente criados como "leitores")
- ✅ Login e logout
- ✅ Recuperação de senha (via console em desenvolvimento)
- ✅ Separação de permissões por grupos (leitores e bibliotecários)
- ✅ Menus diferenciados por tipo de usuário
- ✅ Redirecionamento adequado para usuários não autorizados

### CRUD de Livros (Completo)
- ✅ **Create**: Cadastro com 8 campos + upload de capa
- ✅ **Read**: Listagem com filtros (categoria, disponibilidade)
- ✅ **Update**: Edição de todos os campos
- ✅ **Delete**: Exclusão com confirmação
- ✅ Validações: ano (1000-2025), ISBN (10 ou 13 dígitos)

### Gestão de Empréstimos
- ✅ Solicitar empréstimo (livro fica indisponível automaticamente)
- ✅ Ver "Meus Empréstimos" (cada usuário vê apenas os seus)
- ✅ Devolver livros (livro volta a ficar disponível)
- ✅ Ver "Todos Empréstimos" (apenas bibliotecários)
- ✅ Filtros por status (ativo/finalizado)
- ✅ Validação de data de devolução (deve ser futura)

### Outros Recursos
- ✅ Cadastro de autores com biografia
- ✅ Relacionamento autor-livros (um autor, vários livros)
- ✅ Interface responsiva (desktop e mobile)
- ✅ Mensagens de feedback em todas as ações
- ✅ Design em CSS puro (sem frameworks)
- ✅ **Zero JavaScript** (100% funcional sem JS)
- ✅ Internacionalização pt-BR

---

## ❌ O QUE NÃO FUNCIONOU / LIMITAÇÕES

### Funcionalidades Não Implementadas
- ❌ **Busca textual**: Não há campo de pesquisa por título/autor (apenas filtros de categoria)
- ❌ **Relatórios de atraso**: Sistema não calcula livros em atraso
- ❌ **Multas**: Sem cálculo ou cobrança de multas
- ❌ **Avaliações/Comentários**: Usuários não podem avaliar livros
- ❌ **Reservas**: Não é possível reservar livros emprestados
- ❌ **E-mail real**: Recuperação de senha usa console (não envia e-mails de verdade)

### Limitações Técnicas
- ⚠️ SQLite: Não ideal para produção com múltiplos acessos simultâneos
- ⚠️ Performance: Listagem pode ficar lenta com muitos livros (sem paginação)
- ⚠️ Upload: Tamanho de arquivo limitado pela configuração do servidor

### Bugs Corrigidos
- ✅ Loop de redirecionamento ao acessar páginas de bibliotecário (commit bf3dbea)
- ✅ Lógica de disponibilidade de livros em empréstimos

**Nota**: Todas as limitações foram escolhas conscientes de escopo. As funcionalidades principais (CRUD, autenticação, empréstimos) estão **100% funcionais**.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.13
- Django 4.2 LTS
- HTML5 + CSS3 (sem JavaScript)
- SQLite
- WhiteNoise (servir arquivos estáticos)
- Pillow (upload de imagens)
- Git

---

## 📖 Como Usar o Site

### 1️⃣ Primeiro Acesso

1. Acesse `http://localhost:8000`
2. Clique em **"Cadastrar"** no menu
3. Preencha: username, e-mail e senha
4. Você será automaticamente logado como **leitor**

### 2️⃣ Como Leitor

**Ver Livros:**
- Menu → **"Livros"**
- Use filtros para encontrar (categoria, disponibilidade)
- Clique em **"Ver Detalhes"** para informações completas

**Emprestar Livro:**
- Na página do livro → **"Emprestar"** (se disponível)
- Ou: Menu → **"Meus Empréstimos"** → **"Novo Empréstimo"**
- Selecione livro e data de devolução → Confirmar

**Devolver Livro:**
- Menu → **"Meus Empréstimos"**
- Clique em **"Devolver"** ao lado do empréstimo ativo
- Confirme a devolução

### 3️⃣ Como Bibliotecário

**Tornar-se Bibliotecário** (requer admin):
1. Acesse `/admin` com conta de superusuário
2. Usuários → Selecione o usuário
3. Adicione ao grupo **"bibliotecarios"**
4. Salvar

**Funcionalidades Extras:**
- **Cadastrar Livro**: Menu → "Cadastrar Livro" → Preencher 8 campos
- **Cadastrar Autor**: Menu → "Cadastrar Autor" → Nome + biografia
- **Editar/Excluir**: Na página do livro → Botões "Editar"/"Excluir"
- **Todos Empréstimos**: Menu → "Todos Empréstimos" (vê de todos os usuários)

### 4️⃣ Recuperar Senha

1. Página de login → **"Esqueceu a senha?"**
2. Digite seu e-mail
3. Mensagem aparecerá no console do servidor (em desenvolvimento)

---

## � Como Executar Localmente

### Pré-requisitos
- Python 3.9+ ou Conda
- Git

### Instalação Rápida

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd biblioteca

# 2. Crie ambiente virtual (escolha uma opção)
conda create -n biblioteca_env python=3.13 -y
conda activate biblioteca_env
# OU
python -m venv venv && source venv/bin/activate

# 3. Instale dependências
pip install -r requirements.txt

# 4. Configure banco e grupos
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import Group; Group.objects.get_or_create(name='leitores'); Group.objects.get_or_create(name='bibliotecarios')"

# 5. Crie superusuário
python manage.py createsuperuser

# 6. [OPCIONAL] Popule com dados de teste
python manage.py shell < populate_data.py

# 7. Inicie servidor
python manage.py runserver
```

Acesse: `http://localhost:8000`

### 🧪 Credenciais de Teste

Se você executou `populate_data.py`:

- **Leitor**: `leitor1` / `senha123`
- **Bibliotecário**: `bibliotecario1` / `senha123`
- **Admin**: Use o superusuário criado

**Dados de teste incluem**:
- 5 autores brasileiros (Machado de Assis, Clarice Lispector, etc.)
- 6 livros clássicos da literatura brasileira
- 1 empréstimo ativo de exemplo

---

## 🐳 Executar com Docker (Recomendado)

### ✅ Imagem Publicada no Docker Hub

**Link**: https://hub.docker.com/r/felipekhouri/biblioteca-online

### 🚀 Uso Rápido

```bash
# Baixar e executar
docker pull felipekhouri/biblioteca-online:latest
docker run -p 8000:8000 felipekhouri/biblioteca-online:latest
```

Acesse: **http://localhost:8000**

---

## 🔑 Credenciais para Teste

A imagem Docker **já vem com dados pré-carregados**. Use estas credenciais:

### 👥 Contas Disponíveis

| Tipo | Username | Senha | O que pode fazer |
|------|----------|-------|------------------|
| **🔧 Bibliotecário** | `bibliotecario1` | `senha123` | ✅ **USAR ESTA** - CRUD completo de livros/autores |
| **📖 Leitor** | `leitor1` | `senha123` | Emprestar e devolver livros |
| **👑 Admin** | `admin` | `admin123` | Acesso ao Django Admin (`/admin`) |

### 📚 Dados Incluídos

- ✅ 5 autores brasileiros (Machado de Assis, Clarice Lispector, Jorge Amado, Paulo Coelho, Guimarães Rosa)
- ✅ 6 livros clássicos da literatura brasileira
- ✅ 1 empréstimo ativo de exemplo
- ✅ Grupos configurados (leitores e bibliotecarios)

### 🧪 Como Testar como Bibliotecário

1. Acesse: `http://localhost:8000`
2. Clique em **"Entrar"**
3. Username: `bibliotecario1`
4. Senha: `senha123`
5. ✅ Agora você pode:
   - Cadastrar livros (Menu → "Cadastrar Livro")
   - Cadastrar autores (Menu → "Cadastrar Autor")
   - Editar/Excluir livros
   - Ver todos os empréstimos do sistema

---

## 📖 Como Usar o Site

### 1️⃣ Primeiro Acesso (Criar Conta)

1. Acesse `http://localhost:8000`
2. Clique em **"Cadastrar"**
3. Preencha: username, e-mail e senha
4. Você será automaticamente logado como **leitor**

### 2️⃣ Como Leitor

**Ver Livros:**
- Menu → **"Livros"**
- Use filtros (categoria, disponibilidade)
- Clique em **"Ver Detalhes"**

**Emprestar Livro:**
- Na página do livro → **"Emprestar"** (se disponível)
- Selecione data de devolução → Confirmar

**Devolver Livro:**
- Menu → **"Meus Empréstimos"**
- Clique em **"Devolver"** → Confirmar

### 3️⃣ Como Bibliotecário

Use a conta: `bibliotecario1` / `senha123`

**Funcionalidades Extras:**
- **Cadastrar Livro**: Menu → "Cadastrar Livro" → Preencher 8 campos
- **Cadastrar Autor**: Menu → "Cadastrar Autor" → Nome + biografia
- **Editar/Excluir**: Na página do livro → Botões "Editar"/"Excluir"
- **Todos Empréstimos**: Menu → "Todos Empréstimos" (vê todos os usuários)

---

## 🖥️ Como Executar Localmente (Desenvolvimento)

### Pré-requisitos
- Python 3.9+ ou Conda
- Git

### Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/felipekhouri/INF1407-P1.git
cd INF1407-P1/biblioteca

# 2. Crie ambiente virtual
conda create -n biblioteca_env python=3.13 -y
conda activate biblioteca_env

# 3. Instale dependências
pip install -r requirements.txt

# 4. Configure banco e grupos
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import Group; Group.objects.get_or_create(name='leitores'); Group.objects.get_or_create(name='bibliotecarios')"

# 5. Popular com dados de teste
python manage.py shell < populate_data.py

# 6. Inicie servidor
python manage.py runserver
```

Acesse: `http://localhost:8000`

---

## 📋 Conformidade com Enunciado INF1407

| Requisito | Status |
|-----------|--------|
| Python + Django + HTML + CSS | ✅ |
| **Sem JavaScript** | ✅ |
| CRUD completo | ✅ |
| **Publicação Docker** | ✅ **PUBLICADO** |
| Git + Repositório público | ✅ |
| Login + Acesso por usuário | ✅ |
| Visões diferentes | ✅ |
| README com nomes | ✅ |
| README com escopo | ✅ |
| README com "o que funcionou" | ✅ |
| README com "o que não funcionou" | ✅ |
| README com manual de uso | ✅ |

**Links de Entrega**:
- 🐳 **Docker Hub**: https://hub.docker.com/r/felipekhouri/biblioteca-online
- 📦 **GitHub**: https://github.com/felipekhouri/INF1407-P1

**Estatísticas**:
- ~2.565 linhas de código
- 3 modelos Django
- 15 views
- 16 templates HTML
- Zero linhas de JavaScript
```

Acesse: `http://localhost:8000`

---

---

## 🖥️ Como Executar Localmente (Desenvolvimento)

---

## � Deploy em Produção

### Opção 1: Docker Hub

```bash
# Build e push
docker build -t seu-usuario/biblioteca-online:latest .
docker push seu-usuario/biblioteca-online:latest

# Executar
docker run -p 8000:8000 seu-usuario/biblioteca-online:latest
```

### Opção 2: Render.com (Grátis)

1. Conecte repositório GitHub
2. Build: `pip install -r requirements.txt && python manage.py migrate`
3. Start: `gunicorn biblioteca.wsgi`
4. Variáveis: `SECRET_KEY`, `ALLOWED_HOSTS`, `DEBUG=False`

### Opção 3: Railway

1. Conecte GitHub
2. Railway detecta Django automaticamente
3. Configure variáveis de ambiente

**Arquivos incluídos**: `Dockerfile`, `build.sh`, `requirements.txt`, `.dockerignore`

---

## Conformidade com Enunciado

| Requisito | Status |
|-----------|--------|
| Python + Django + HTML + CSS | ✅ |
| **Sem JavaScript** | ✅ |
| CRUD completo | ✅ |
| Publicação (Docker/Web) | ✅ Pronto |
| Git + Repositório público | ✅ |
| Login + Acesso por usuário | ✅ |
| Visões diferentes | ✅ |
| README com nomes | ✅ |
| README com escopo | ✅ |
| README com "o que funcionou" | ✅ |
| README com "o que não funcionou" | ✅ |
| README com manual de uso | ✅ |

**Estatísticas**:
- ~2.565 linhas de código
- 3 modelos Django
- 15 views
- 16 templates HTML
- Zero linhas de JavaScript
