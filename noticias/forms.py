# noticias/forms.py
from django import forms
from .models import Noticia, Comentario

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'resumo', 'conteudo', 'imagem', 'categoria']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'conteudo']
