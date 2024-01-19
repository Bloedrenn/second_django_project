from django.shortcuts import render

# Create your views here.


def say_hello(request):
    return render(request, 'main/hello.html')


def say_main(request):
    return render(request, 'main/main.html')
