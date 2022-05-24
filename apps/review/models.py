from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.product.models import Products


class Review(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='product', verbose_name='Автор')
    product = models.ForeignKey(Products, verbose_name='Продукт', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текс')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.author} {self.text}'
    