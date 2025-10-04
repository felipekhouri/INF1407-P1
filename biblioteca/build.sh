#!/bin/bash

# Script de build para produção

echo "🔧 Instalando dependências..."
pip install -r requirements.txt

echo "📦 Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

echo "🗄️  Executando migrações..."
python manage.py migrate

echo "👥 Criando grupos de usuários..."
python manage.py shell -c "from django.contrib.auth.models import Group; Group.objects.get_or_create(name='leitores'); Group.objects.get_or_create(name='bibliotecarios')"

echo "✅ Build concluído com sucesso!"
