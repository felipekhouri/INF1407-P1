from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Autor(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome")
    bio = models.TextField(blank=True, verbose_name="Biografia")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Livro(models.Model):
    CATEGORIAS = [
        ('ficcao', 'Ficção'),
        ('nao_ficcao', 'Não-Ficção'),
        ('romance', 'Romance'),
        ('suspense', 'Suspense'),
        ('biografia', 'Biografia'),
        ('tecnico', 'Técnico'),
        ('infantil', 'Infantil'),
        ('outros', 'Outros'),
    ]

    titulo = models.CharField(max_length=300, verbose_name="Título")
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name='livros')
    categoria = models.CharField(max_length=50, choices=CATEGORIAS, verbose_name="Categoria")
    ano_publicacao = models.IntegerField(verbose_name="Ano de Publicação")
    isbn = models.CharField(max_length=17, unique=True, verbose_name="ISBN")
    sinopse = models.TextField(blank=True, verbose_name="Sinopse")
    editora = models.CharField(max_length=200, verbose_name="Editora")
    capa = models.ImageField(upload_to='capas/', blank=True, null=True, verbose_name="Capa")
    disponibilidade = models.BooleanField(default=True, verbose_name="Disponível")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.titulo} - {self.autor.nome}"

    def clean(self):
        # Validação do ano de publicação
        ano_atual = timezone.now().year
        if self.ano_publicacao < 1000 or self.ano_publicacao > ano_atual:
            raise ValidationError(f'Ano de publicação deve estar entre 1000 e {ano_atual}.')

        # Validação básica do ISBN (apenas dígitos e hífens)
        isbn_limpo = self.isbn.replace('-', '')
        if not isbn_limpo.isdigit():
            raise ValidationError('ISBN deve conter apenas números e hífens.')
        if len(isbn_limpo) not in [10, 13]:
            raise ValidationError('ISBN deve ter 10 ou 13 dígitos.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('finalizado', 'Finalizado'),
    ]

    livro = models.ForeignKey(Livro, on_delete=models.PROTECT, related_name='emprestimos')
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name='emprestimos')
    data_inicio = models.DateField(auto_now_add=True, verbose_name="Data de Início")
    data_fim_prevista = models.DateField(verbose_name="Data Prevista para Devolução")
    data_fim_real = models.DateField(null=True, blank=True, verbose_name="Data Real de Devolução")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo', verbose_name="Status")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.username} ({self.status})"

    def clean(self):
        # Validar se o livro está disponível (apenas para novos empréstimos)
        if not self.pk and not self.livro.disponibilidade:
            raise ValidationError('Este livro não está disponível para empréstimo.')

        # Validar data fim prevista
        if self.data_fim_prevista <= timezone.now().date():
            raise ValidationError('A data prevista para devolução deve ser futura.')

    def save(self, *args, **kwargs):
        if not self.pk:  # Novo empréstimo
            self.full_clean()
            # Marcar livro como indisponível
            self.livro.disponibilidade = False
            self.livro.save()
        super().save(*args, **kwargs)

    def finalizar(self):
        """Finaliza o empréstimo e marca o livro como disponível"""
        self.status = 'finalizado'
        self.data_fim_real = timezone.now().date()
        self.livro.disponibilidade = True
        self.livro.save()
        self.save()
