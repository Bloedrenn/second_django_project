from django.shortcuts import render
from .models import Post

# Create your views here.

menu = [
    {'title': 'Посты', 'path_name': 'main:get_posts'},
    # {'title': 'Создать пост', 'path_name': 'main:add_post'},
    # {'title': 'Контакты', 'path_name': 'main:contacts'},
    # {'title': 'О сайте', 'path_name': 'main:about'}
]


def say_hello(request):
    return render(request, 'main/hello.html')


def say_main(request):
    return render(request, 'main/main.html')


def get_posts(request):
    posts = Post.objects.all()

    context = {'posts': posts, 'menu': menu}

    return render(request, template_name='main/posts.html', context=context)
