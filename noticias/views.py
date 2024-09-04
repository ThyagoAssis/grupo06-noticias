from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from .models import Noticia, Comentario
from .forms import NoticiaForm, ComentarioForm


class NoticiaListView(ListView):
    model = Noticia
    template_name = 'noticias/noticia_list.html'
    context_object_name = 'noticias'


class NoticiaDetailView(DetailView):
    model = Noticia
    template_name = 'noticias/noticia_detail.html'
    context_object_name = 'noticia'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all()  # Pega todos os comentários associados à notícia
        context['comentario_form'] = ComentarioForm()  # Adiciona o formulário de comentário ao contexto
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.noticia = self.object  # Relaciona o comentário com a notícia
            comentario.save()
            return redirect(reverse('noticia_detail', kwargs={'pk': self.object.pk}))
        return self.render_to_response(self.get_context_data(comentario_form=form))


class NoticiaCreateView(CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/noticia_form.html'
    success_url = reverse_lazy('noticia_list')


class NoticiaUpdateView(UpdateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticias/noticia_form.html'
    success_url = reverse_lazy('noticia_list')


class NoticiaDeleteView(DeleteView):
    model = Noticia
    template_name = 'noticias/noticia_confirm_delete.html'
    success_url = reverse_lazy('noticia_list')

