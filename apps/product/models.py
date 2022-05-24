from django.db import models


class Category(models.Model):
    slug = models.SlugField(max_length=155, primary_key=True, verbose_name='Слаг')
    name = models.CharField(max_length=155, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название продукта')
    desc = models.TextField(verbose_name='Описание')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')
    category = models.ForeignKey(Category, default=0, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Продукта'
        verbose_name_plural = 'Продукты'
#
    def __str__(self):
        return self.title
