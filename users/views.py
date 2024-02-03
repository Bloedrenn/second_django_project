from django.shortcuts import render
from .forms import UserRegistrationForm
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
