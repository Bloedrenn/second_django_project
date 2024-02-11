from django.urls import path
from .views import (
    index, get_posts, get_post,
    create_post, edit_post, delete_post,
    search, contacts, about
)

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('posts/', get_posts, name='get_posts'),
    path('posts/<int:pk>/', get_post, name='get_post'),
    path('create_post/', create_post, name='create_post'),
    path('posts/<int:pk>/edit/', edit_post, name='edit_post'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),
    path('posts/search/', search, name="search"),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about')
]
