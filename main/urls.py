from django.urls import path
from .views import index, get_posts, get_post, create_post, contacts, about

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('posts/', get_posts, name='get_posts'),
    path('posts/<int:pk>/', get_post, name='get_post'),
    path('create_post/', create_post, name='create_post'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about')
]
