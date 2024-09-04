# noticias/urls.py
from django.urls import path
from .views import NoticiaListView, NoticiaDetailView, NoticiaCreateView, NoticiaUpdateView, NoticiaDeleteView

urlpatterns = [
    path('', NoticiaListView.as_view(), name='noticia_list'),
    path('noticia/<int:pk>/detail', NoticiaDetailView.as_view(), name='noticia_detail'),
    path('noticia/add/', NoticiaCreateView.as_view(), name='noticia_add'),
    path('noticia/<int:pk>/edit/', NoticiaUpdateView.as_view(), name='noticia_edit'),
    path('noticia/<int:pk>/delete/', NoticiaDeleteView.as_view(), name='noticia_delete'),
]
