FROM python:3.13-slim

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn

# Copiar projeto
COPY . .

# Coletar arquivos estáticos
RUN python manage.py collectstatic --no-input

# Criar grupos
RUN python manage.py shell -c "from django.contrib.auth.models import Group; Group.objects.get_or_create(name='leitores'); Group.objects.get_or_create(name='bibliotecarios')"

# Expor porta
EXPOSE 8000

# Comando de inicialização
CMD ["sh", "-c", "python manage.py migrate && gunicorn biblioteca.wsgi:application --bind 0.0.0.0:8000"]
