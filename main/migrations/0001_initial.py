# Generated by Django 5.0.1 on 2024-02-04 13:26

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст поста')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/', verbose_name='Изображение поста')),
                ('created_date_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('publication_date', models.DateTimeField(editable=False, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['title'],
            },
        ),
    ]
