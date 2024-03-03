from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    slug = models.CharField(max_length=150, verbose_name='slug')
    body = models.TextField(verbose_name='содержимое')
    picture = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Статус')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}. Просмотрено {self.views_count} раз'

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'юлоговые записи'
