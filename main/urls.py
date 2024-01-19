from django.urls import path
from .views import say_hello, say_main

urlpatterns = [
    path('', say_main),
    path('hello/', say_hello)
]
