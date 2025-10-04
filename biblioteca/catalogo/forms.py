from django import forms
from .models import Livro, Autor, Emprestimo
from datetime import date, timedelta


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'bio']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria', 'ano_publicacao', 'isbn',
                  'sinopse', 'editora', 'capa']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'ano_publicacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 978-3-16-148410-0'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'editora': forms.TextInput(attrs={'class': 'form-control'}),
            'capa': forms.FileInput(attrs={'class': 'form-control'}),
        }


class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['livro', 'data_fim_prevista']
        widgets = {
            'livro': forms.Select(attrs={'class': 'form-control'}),
            'data_fim_prevista': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'},
                format='%Y-%m-%d'
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mostrar apenas livros disponíveis
        self.fields['livro'].queryset = Livro.objects.filter(disponibilidade=True)
        # Definir data mínima como amanhã
        self.fields['data_fim_prevista'].initial = date.today() + timedelta(days=7)
        self.fields['data_fim_prevista'].widget.attrs['min'] = (date.today() + timedelta(days=1)).isoformat()
