# Generated by Django 5.0.1 on 2024-01-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
    ]