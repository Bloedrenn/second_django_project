# Generated by Django 5.0.1 on 2024-01-19 19:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_post_publication_date_alter_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date_time',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]