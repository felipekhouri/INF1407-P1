# Stage 1: Build
FROM python:3.13-slim

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copiar código do projeto
COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --no-input

# Executar migrations ANTES de criar grupos
RUN python manage.py migrate

# Criar grupos
RUN python manage.py shell -c "from django.contrib.auth.models import Group; Group.objects.get_or_create(name='leitores'); Group.objects.get_or_create(name='bibliotecarios')"

# Criar superuser padrão (para facilitar testes)
RUN python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@biblioteca.com', 'admin123') if not User.objects.filter(username='admin').exists() else None"

# Popular dados de exemplo SEMPRE (garante credenciais de teste)
RUN python manage.py shell < populate_data.py

# Expor porta
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "biblioteca.wsgi:application"]
