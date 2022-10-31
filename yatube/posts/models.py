from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название группы"
    )
    slug = models.SlugField(
        null=True,
        unique=True,
        verbose_name="Адрес"
    )
    description = models.TextField(
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст"
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Автор",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='group',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.text
