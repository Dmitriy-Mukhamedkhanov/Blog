from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/", verbose_name="Изображение")
    age = models.IntegerField(blank=True, null=True, verbose_name="Возраст")

    def __str__(self):
        return f'{self.username} {self.last_name}'

    class Meta:
        db_table = 'user'
        verbose_name = 'пользователи'
        verbose_name_plural = 'пользователи'


class Photo(models.Model):
    name = models.CharField(max_length=150, verbose_name='название фото')
    description = models.TextField(verbose_name='описание фото')
    published = models.DateField(auto_now=True, verbose_name='дата публикации фото')
    image = models.ImageField(upload_to="photos/", verbose_name="Изображение")
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'photo'
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'


class Comment(models.Model):
    published_comment = models.DateField(auto_now=True, verbose_name='дата публикации комментария')
    text_comment = models.TextField(verbose_name='текст комментария')
    author_comment = models.TextField('Имя', max_length=20)
    image_comment = models.ForeignKey('Photo', on_delete=models.CASCADE, related_name='comment_photo',
                                      verbose_name='добавить фото')

    def __str__(self):
        return f'{self.author_comment},{self.text_comment}'

    class Meta:
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Likes(models.Model):
    ip = models.CharField('IP-адрес', max_length=100)
    pos = models.ForeignKey(Photo, verbose_name='Публикация', on_delete=models.CASCADE)
