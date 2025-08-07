from django.shortcuts import render
from .models import Post

def lista_de_posts(request):
    posts = Post.objects.all().order_by('-data_criacao')
    contexto = {'posts': posts}
    return render(request, 'blog/lista_de_posts.html')

def detalhe_do_post(request, pk):
    post = Post.objects.get(pk=pk)
    contexto = {'post': post}
    return render(request, 'blog/detalhe_do_post.html', contexto)
