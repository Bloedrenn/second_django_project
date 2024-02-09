from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(blank=True, null=True, verbose_name='Текст поста')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True, verbose_name='Изображение поста')
    created_date_time = models.DateTimeField(default=timezone.now, editable=False)
    publication_date = models.DateTimeField(null=True, editable=False)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['title'] # '-title' - сортировка по убыванию

    def publish(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
