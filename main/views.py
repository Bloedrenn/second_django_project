from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

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


@login_required
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

            post.author = request.user
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            post.image = form.cleaned_data['image']
            
            post.publish()

            url = reverse('main:get_posts')

            return redirect(url)
        

def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
        
            return redirect('main:get_post', pk=pk)
        
    elif request.method == 'GET':
        form = PostForm(instance=post)

        title = 'Редактировать пост'

        context = {'menu': menu, 'title': title, 'form': form}

        return render(request, 'main/edit_post.html', context)
    

def delete_post(request, pk):
    post = Post.objects.filter(pk=pk).first()
    
    if request.method == 'GET':
        title = 'Удалить пост'

        context = {'menu': menu, 'title': title}

        return render(request, 'main/delete_post.html', context)

    elif request.method == 'POST':
        if "delete" in request.POST:
            post.delete()

            return redirect('main:get_posts')
        
        elif "cancel" in request.POST:
            return redirect('main:get_post', pk)
        

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
