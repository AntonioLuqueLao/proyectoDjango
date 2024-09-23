from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.

def Blog(request):
    posts=Post.objects.all()
    categorias=Categoria.objects.all()

    print(categorias)
    return render(request, "blog/Blog.html", {"posts": posts, "categorias": categorias})

def Categorias(request, id_categorias):
    categoria=Categoria.objects.get(id=id_categorias)
    posts=Post.objects.filter(categorias=categoria)
    print(posts)
    return render(request, "blog/categorias.html", {"posts": posts, "categoria": categoria})