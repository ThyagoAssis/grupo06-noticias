# noticias/models.py
from django.db import models

class Noticia(models.Model):
    CATEGORIAS = [
        ('POLITICA', 'Política'),
        ('ARTE', 'Arte'),
        ('MEIO_AMBIENTE', 'Meio Ambiente'),
        ('TIROTEIO', 'Tiroteio'),
        ('ACIDENTE', 'Acidente'),
        ('ROCK_IN_RIO', 'Rock in Rio'),
        ('FUTEBOL', 'Futebol'),
        ('ESPORTES','Esportes'),
        ('OUTROS', 'Outros'),
    ]

    titulo = models.CharField(max_length=200)
    resumo = models.TextField()
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='noticias/')
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    noticia = models.ForeignKey(Noticia, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário de {self.autor} em {self.noticia.titulo}'
