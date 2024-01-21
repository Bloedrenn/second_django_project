from django.urls import path
from .views import say_hello, say_main, get_posts

app_name = 'main'

urlpatterns = [
    path('', say_main),
    path('hello/', say_hello),
    path('posts/', get_posts, name='get_posts')
]
