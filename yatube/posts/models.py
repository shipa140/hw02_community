from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель для группы."""

    title = models.CharField(
        max_length=200,
        verbose_name='Имя'
    )
    slug = models.SlugField(
        max_length=40,
        verbose_name='Адрес', unique=True
    )
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель для постов."""

    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Сообщество',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts'
    )

    class Meta:
        ordering = ('-pub_date',)
