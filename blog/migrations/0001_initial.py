# Generated by Django 4.2.1 on 2024-03-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Наименование')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Превью')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='Статус')),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'блоговая запись',
                'verbose_name_plural': 'юлоговые записи',
            },
        ),
    ]