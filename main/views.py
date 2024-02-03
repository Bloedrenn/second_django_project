from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

menu = [
    {'url_title': 'Блог', 'path_name': 'main:index'},
    {'url_title': 'Посты', 'path_name': 'main:get_posts'},
    {'url_title': 'Создать пост', 'path_name': 'main:create_post'},
    {'url_title': 'Контакты', 'path_name': 'main:contacts'},
    {'url_title': 'О сайте', 'path_name': 'main:about'}
]


def get_posts(request):
    posts = Post.objects.all()

    title = 'Посты'

    context = {'menu': menu, 'title': title, 'posts': posts}

    return render(request, template_name='main/posts.html', context=context)


def index(request):
    title = 'Блог'

    return render(request, 'main/index.html', context={'menu': menu, 'title': title})


def create_post(request):
    if request.method == 'GET':
        form = PostForm()

        title = 'Создать пост'

        context = {'menu': menu, 'title': title, 'form': form}

        return render(request, 'main/create_post.html', context=context)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = Post()

            post.author = form.cleaned_data['author']
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            post.image = form.cleaned_data['image']
            
            post.publish()

            return redirect('/posts/')
        

def get_post(request, pk):
    post = Post.objects.get(pk=pk)

    title = f'{post.title}'

    context = {'menu': menu, 'title': title, 'post': post}

    return render(request, 'main/post.html', context=context)


def contacts(request):
    title = 'Контакты'

    context = {'menu': menu, 'title': title}

    return render(request, 'main/contacts.html', context=context)


def about(request):
    title = 'О сайте'

    context = {'menu': menu, 'title': title}

    return render(request, 'main/about.html', context=context)
