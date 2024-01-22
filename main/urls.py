from django.urls import path
from .views import index, get_posts, create_post, contacts, about

app_name = 'main'

urlpatterns = [
    path('', index),
    path('posts/', get_posts, name='get_posts'),
    path('create_post/', create_post, name='create_post'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about')
]
