from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

menu = [
    {'url_title': 'Посты', 'path_name': 'main:get_posts'},
    {'url_title': 'Создать пост', 'path_name': 'main:create_post'},
    {'url_title': 'Контакты', 'path_name': 'main:contacts'},
    {'url_title': 'О сайте', 'path_name': 'main:about'}
]


def get_posts(request):
    posts = Post.objects.all()

    title = 'Посты' #

    context = {'menu': menu, 'title': title, 'posts': posts} # +'title': title

    return render(request, template_name='main/posts.html', context=context)


def index_root(request):
    title = 'Главная страница'

    context = {'menu': menu, 'title': title}

    return render(request, 'main/index_root.html', context=context)


def index(request):
    title = 'Блог'

    return render(request, 'main/index.html', context={'menu': menu, 'title': title})


def create_post(request):
    if request.method == 'GET':
        form = PostForm()

        title = 'Создать пост'

        context = {'menu': menu, 'title': title, 'form': form}

        return render(request, 'main/create_post.html', context=context)
    
    #
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = Post()

            post.author = form.cleaned_data['author']
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            
            post.publish()

            return get_posts(request)
    #


def contacts(request):
    title = 'Контакты'

    context = {'menu': menu, 'title': title}

    return render(request, 'main/contacts.html', context=context)


def about(request):
    title = 'О сайте'

    context = {'menu': menu, 'title': title}

    return render(request, 'main/about.html', context=context)
