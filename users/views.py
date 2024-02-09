from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from blog.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.models import User
from main.views import menu

# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(form.cleaned_data['password'])

            user.save()

        title = 'Регистрация завершена'

        context = {'menu': menu, 'title': title, 'user': user}

        return render(request, 'users/registration_completed.html', context=context)
    
    form = UserRegistrationForm()

    title = 'Регистрация пользователя'

    context = {'menu': menu, 'title': title, 'form': form}

    return render(request, 'users/registration.html', context=context)


def log_in(request):
    form = AuthenticationForm(data=None or request.POST)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect(LOGIN_REDIRECT_URL)

            # Альтернатива:
            # url = request.GET.get('next')
            #
            # return redirect(url)
    
    title = 'Войти'

    context = {'menu': menu, 'title': title, 'form': form}

    return render(request, 'users/log_in.html', context=context)


def log_out(request):
    logout(request)

    url = reverse('main:index')

    return redirect(url)


def get_user_info(request, pk):
    user = User.objects.get(pk=pk)

    title = f'{user.first_name} {user.last_name}'

    context = {'menu': menu, 'title': title, 'user': user}

    return render(request, 'users/user.html', context=context)
